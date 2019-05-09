from django.test import TestCase
from .models import Ship
from django.db.utils import IntegrityError

class ShipTestCase(TestCase):
    def setUp(self):
        Ship.objects.create(name="ship1", imo_number="1234567")
        Ship.objects.create(name="ship2", imo_number="7654321")

    def test_ship_str(self):
        s1 = Ship.objects.get(name="ship1")
        s2 = Ship.objects.get(name="ship2")
        self.assertEqual(str(s1), 'ship1 (1234567)')
        self.assertEqual(str(s2), 'ship2 (7654321)')

    def test_ship_integrity(self):
        s1 = Ship.objects.get(name="ship1")
        s3 = Ship(name=s1.name, imo_number=s1.imo_number)
        with self.assertRaises(IntegrityError):
            s3.save()


