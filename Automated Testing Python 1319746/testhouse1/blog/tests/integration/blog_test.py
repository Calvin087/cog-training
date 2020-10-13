from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):

    def test_create_post_in_blog(self):
        new_blog = Blog("Test Title", "Test Author")
        new_blog.create_post("Test Post", "Test Content")

        self.assertEqual(len(new_blog.posts), 1)
        self.assertEqual(new_blog.posts[0].title, "Test Post")
        self.assertEqual(new_blog.posts[0].content, "Test Content")

    def test_json(self):
        new_blog = Blog("Test Title", "Test Author")
        new_blog.create_post("Test Post", "Test Content")
        
        expected = {'title': 'Test Title', 'author': 'Test Author', 'posts': [{}]}

        self.assertDictEqual()