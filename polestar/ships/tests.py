from django.test import TestCase
from .models import Ship, Position
from django.db.utils import IntegrityError
from django.utils import timezone

from django.core import management
from django.core.management.base import CommandError
import io


class ShipTestCase(TestCase):
    def setUp(self):
        Ship.objects.create(name="ship1", imo_number="9632179")
        Ship.objects.create(name="ship2", imo_number="9247455")

    def test_ship_str(self):
        s1 = Ship.objects.get(name="ship1")
        s2 = Ship.objects.get(name="ship2")
        self.assertEqual(str(s1), 'ship1 (9632179)')
        self.assertEqual(str(s2), 'ship2 (9247455)')

    def test_ship_integrity(self):
        s1 = Ship.objects.get(name="ship1")
        s3 = Ship(name=s1.name, imo_number=s1.imo_number)
        with self.assertRaises(IntegrityError):
            s3.save()

    def test_created_updated(self):
        s1 = Ship.objects.get(name="ship1")
        s2 = Ship.objects.get(name="ship2")
        self.assertNotEqual(s1.updated, s1.created)
        self.assertTrue(s1.updated < s2.updated)
        s1.save()
        self.assertTrue(s1.updated > s2.updated)


class PositionTestCase(TestCase):
    def setUp(self):
        s = Ship.objects.create(name="ship1", imo_number="9632179")
        s.positions.create(date=timezone.now(), latitude=17.88356590271, longitude=-63.2951011657715)

    def test_position_str(self):
        s1 = Ship.objects.get(name="ship1")
        p1 = Position.objects.first()
        self.assertIn(p1, s1.positions.all())
        p2 = Position.objects.create(date=timezone.now(), latitude=17.88356590271, longitude=-63.2951011657715)
        s1.positions.add(p2)
        self.assertIn(p2, s1.positions.all())
        s1.positions.remove(p2)
        self.assertNotIn(p2, s1.positions.all())

class PositionManagementCase(TestCase):
    def setUp(self):
        Ship.objects.create(name="ship1", imo_number="9632179")
        Ship.objects.create(name="ship2", imo_number="9247455")
        Ship.objects.create(name="ship3", imo_number="9595321")

    def test_command(self):
        out = io.StringIO()
        management.call_command('import_data', stdout=out)
        self.assertIn("Successfully imported", out.getvalue())
