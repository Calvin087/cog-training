from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog

class AppTest(TestCase):
    
    def test_menu_prints_prompt(self):

        with patch('builtins.input') as mocked_input:
            app.menu()
            mocked_input.assert_called_with("Enter 'c' to create a blog, 'l' to list blogs, 'r' to read one, 'p' to create a post, or 'q' to quit: ")

    def test_menu_calls_print_blogs(self):
        with patch('app.print_blog_posts') as mocked_print_blogs:
            # stops and waits for user input

            with patch('builtins.input', return_value='q'):
                # passes through user input and doesn't require it.
                # return value passes a mocked input as 'q'
                app.menu()
                mocked_print_blogs.assert_called()

    def test_print_blogs(self):

        blog = Blog('Test', 'Test Author')
        # importing from blog, section
        # Then sliding over to app and printing the blog posts
        
        app.blogs = {'TestAasd': blog}
        # Confused, are we now creating a collection of blogs
        # Each with a number of blog posts??

        with patch('builtins.print') as mocked_print:
            # patching the print function as mocked print
            # the print function in app.py is being **REPLACED** by
            # my patched version then we're checking if it was called
            # PRINT is never really called, an imposter of Print, runs.
            # NO console check has been done.
        
            app.print_blog_posts()
            mocked_print.assert_called_with('- Test by Test Author (0 posts)')
