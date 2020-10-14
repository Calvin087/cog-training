from tests.system.test_base import BaseTest
import json

class TestHome(BaseTest):
    def test_home(self):
        with self.app() as c:
        # self.app is being pulled from based test where we're
        # initiating app.test_client
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
            