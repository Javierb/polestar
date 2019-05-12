from django.test import TestCase
from django.test import Client
from polestar.ships.models import Ship, Position
from django.utils import timezone

class APITest(TestCase):
    fixtures = ['ships.json',]

    def test_ship_list(self):
        client = Client()
        response = client.get('/api/ships/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Mathilde Maersk', response.content)
    
    def test_post_ships(self):
        c = Client()
        response = c.post('/api/ships/', {'name': 'hola', 'imo': 12345})
        self.assertEqual(response.status_code, 405)

    def test_url_trailing(self):
        client = Client()
        response = client.get('/api/ships')
        self.assertEqual(response.status_code, 301)

    def test_positions_list(self):
        client = Client()
        response = client.get('/api/positions/')
        self.assertEqual(response.status_code, 404)
    
    def test_positions_imo(self):
        s = Ship.objects.get(imo_number="9632179")
        client = Client()
        response = client.get('/api/positions/{}/'.format(s.imo_number))
        self.assertEqual(response.status_code, 200)
    
    def test_positions_content(self):
        s = Ship.objects.get(imo_number="9632179")
        Position.objects.create(ship=s, date=timezone.now(), latitude=17.88356590271, longitude=-63.2951011657715)
        client = Client()
        response = client.get('/api/positions/{}/'.format(s.imo_number))
        self.assertIn(b'latitude', response.content)


    
    