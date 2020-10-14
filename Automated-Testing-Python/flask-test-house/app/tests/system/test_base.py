from unittest import TestCase
from app import app

class BaseTest(TestCase):
    def setUp(self):
        # this runs before each test.
        app.testing = True
        # either on every function we write or
        # on the setUp function, it tells flask
        # that we're always testing.
        # Errors are going to be shown differently / settings.

        self.app = app.test_client
        