from unittest import TestCase
from app import app
import json

class TestHome(TestCase):
    def test_home(self):
        with app.test_client() as c:
            response = c.get('/')

        # Test client comes from Flask
        # Doesn't run everything in the bg
        # making a request to the app

            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                json.loads(response.get_data()),
                {'message': 'Hello World'}
            )
            # Load S means load string, not loads plural.
            # This turns our dictionary into a json string from app.py.
            