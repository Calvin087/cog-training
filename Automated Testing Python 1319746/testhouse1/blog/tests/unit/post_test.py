from unittest import TestCase
from post import Post

class PostTest(TestCase):
    #we're inheriting the test case api methods.
    # it's now referenced as self after inheritance.

    def test_create_post(self):
        p = Post("Test Title", "Test Content Here")

        self.assertEqual("Test Title", p.title)
        # Make sure that the string we're passing
        # is the same as p.title

        self.assertEqual("Test Content Here", p.content)