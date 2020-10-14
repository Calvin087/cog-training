from unittest import TestCase
from post import Post

class PostTest(TestCase):
    #we're inheriting the test case api methods.
    # it's now referenced as self after inheritance.

    def test_create_post(self):
        new_post = Post("Test Title", "Test Content Here")

        self.assertEqual("Test Title", new_post.title)
        # Make sure that the string we're passing
        # is the same as p.title

        self.assertEqual("Test Content Here", new_post.content)

    def test_json(self):
        new_post = Post("Test Title", "Test Content Here")
        expected = {'title': 'Test Title', 'content': 'Test Content Here'}

        self.assertDictEqual(expected, new_post.json())
        # .json is a function on the object we're testing, hence ()
        # checking if the dictionary's content are the same.
        # assertEqual only will check if the object is the same
        # in memory, which we don't want.