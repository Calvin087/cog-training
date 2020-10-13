from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):

    def test_create_blog(self):
        new_blog = Blog("Test Title", "Test Author")

        self.assertEqual("Test Title", new_blog.title)
        self.assertEqual("Test Author", new_blog.author)
        self.assertListEqual([], new_blog.posts)

    def test_repr(self):
        new_blog = Blog("Test Title", "Test Author")

        self.assertEqual(new_blog.__repr__(), "Test Title by Test Author (0 posts)")