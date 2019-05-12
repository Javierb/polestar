from django.test import TestCase
from django.core.management.base import CommandError
from django.db.utils import IntegrityError
from django.utils import timezone
from django.core import management
from .models import Ship, Position
import io


class BaseShipTestCase(TestCase):
    fixtures = ['ships.json',]
    

class ShipTestCase(BaseShipTestCase):
    def test_ship_str(self):
        s1 = Ship.objects.get(imo_number=9632179)
        self.assertEqual(str(s1), 'Mathilde Maersk (9632179)')

    def test_ship_integrity(self):
        s1 = Ship.objects.get(imo_number=9632179)
        s3 = Ship(name=s1.name, imo_number=s1.imo_number)
        with self.assertRaises(IntegrityError):
            s3.save()

    def test_created_updated(self):
        s1 = Ship.objects.get(imo_number=9632179)
        s2 = Ship.objects.get(imo_number=9247455)
        self.assertNotEqual(s1.updated, s1.created)
        s1.save()
        self.assertTrue(s1.updated > s2.updated)


class PositionTestCase(BaseShipTestCase):
    def test_position_integrity(self):
        t = timezone.now()
        s1 = Ship.objects.get(imo_number=9632179)
        Position.objects.create(ship=s1, date=t, latitude=17.88356590271, longitude=-63.2951011657715)
        self.assertEqual(s1.positions.count(), 1)

        with self.assertRaises(IntegrityError):
            Position.objects.create(ship=s1, date=t, latitude=17.88356590271, longitude=-63.2951011657715)


class PositionManagementCase(BaseShipTestCase):
    def test_command(self):
        out = io.StringIO()
        management.call_command('import_data', stdout=out)
        self.assertIn("Successfully imported", out.getvalue())
