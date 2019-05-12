from django.test import TestCase
from django.test import Client
from polestar.ships.models import Ship, Position
from django.utils import timezone

class APITest(TestCase):
    """
    API tests that loads the ships from the fixture.
    """
    fixtures = ['ships.json',]

    def test_ship_list(self):
        """
        Test the that ships end point content data.
        """
        client = Client()
        response = client.get('/api/ships/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Mathilde Maersk', response.content)
    
    def test_post_ships(self):
        """
        Test that post to the ships endpoint is not allowed
        """
        c = Client()
        response = c.post('/api/ships/', {'name': 'hola', 'imo': 12345})
        self.assertEqual(response.status_code, 405)

    def test_url_trailing(self):
        """
        Test that the url trailing is needed at the ships endpoint.
        """
        client = Client()
        response = client.get('/api/ships')
        self.assertEqual(response.status_code, 301)

    def test_positions_list(self):
        """
        Test that the positions endpoint doesn't without providing an imo
        """
        client = Client()
        response = client.get('/api/positions/')
        self.assertEqual(response.status_code, 404)
    
    def test_positions_imo(self):
        """
        Test that positions endpoint return a valid status code if an imo is provided.
        """
        s = Ship.objects.get(imo_number="9632179")
        client = Client()
        response = client.get('/api/positions/{}/'.format(s.imo_number))
        self.assertEqual(response.status_code, 200)
    
    def test_positions_content(self):
        """
        Test the content returned at the positions end point.
        """
        s = Ship.objects.get(imo_number="9632179")
        Position.objects.create(ship=s, date=timezone.now(), latitude=17.88356590271, longitude=-63.2951011657715)
        client = Client()
        response = client.get('/api/positions/{}/'.format(s.imo_number))
        self.assertIn(b'latitude', response.content)


    
    