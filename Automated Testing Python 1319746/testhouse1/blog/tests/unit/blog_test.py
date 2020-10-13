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

    def test_repr_multi_posts(self):
        new_blog = Blog("Test Title", "Test Author")
        new_blog.posts = ["test post"]
        my_blog = Blog("Calvin's Blog", "Calvin T")
        my_blog.posts = ["A day in the life", "How I set up projects", "Last Day"]


        self.assertEqual(new_blog.__repr__(), "Test Title by Test Author (1 post)")
        self.assertEqual(my_blog.__repr__(), "Calvin's Blog by Calvin T (3 posts)")