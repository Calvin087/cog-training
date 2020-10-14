from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog
from post import Post

class AppTest(TestCase):

    def setUp(self):
        blog = Blog('Test', 'Test Author')
        # importing from blog, section
        # Then sliding over to app and printing the blog posts

        app.blogs = {'Test': blog}
        # sending a dictionary with the key of "TestAasd"
        # and value of the newly created blog object.

    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_create_blog') as mocked_ask_create_blog:
                mocked_input.side_effect = ('c', 'Test Create Blog', 'Test Author', 'q')
                # checking if the flow for c creates the right result.
                # typing c asks you to create a new blog with name and author.
                # we then provide an input as side effect, author and then q to cancel.

                app.menu()

                mocked_ask_create_blog.assert_called()

    
    def test_menu_prints_prompt(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            # stops and waits for user input

            with patch('builtins.input', return_value='q'):
                # passes through user input and doesn't require it.
                # return value passes a mocked input as 'q'
                app.menu()
                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print:
            # patching the print function as mocked print
            # the print function in app.py is being **REPLACED** by
            # my patched version then we're checking if it was called
            # PRINT is never really called, an imposter of Print, runs.
            # NO console check has been done.
        
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Test Author (0 posts)')

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('My Blog Title', 'Test Author')
            # This uses the first argument the first time it's called
            # The second the second and so on
            # Mimics the user input of Enter a title, Enter your name.
            # return_value='' only passes one, side effect gives many.

            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get('My Blog Title'))
            # when we GET a blog with KEY 'Test' from app.blogs is not NONE
            # Fails before creating side effect
    
    def test_ask_read_blog(self):

        with patch('builtins.input', return_value='Test'):
            with patch('app.print_posts') as mocked_print_posts:
            # We're mocking the print_posts function from app.py
            # we're then naming that mocked_print_posts as a variabe?
                
                app.ask_read_blog()
                # What happens when this function runs?
                
                mocked_print_posts.assert_called_with(app.blogs['Test'])

    def test_print_posts(self):
        blog = app.blogs['Test']
        blog.create_post('Test Post', 'Test Content')
        # adding post to blog



        with patch('app.print_post') as mocked_print_post:
            app.print_posts(blog)

            mocked_print_post.assert_called_with(blog.posts[0])
            # calling the list of posts we made above and asking for the first one.

    def test_print_post(self):
        post_to_print = Post('Post to Print', 'Post Content to Print')
        # creating a single post to send to print

        expected_post_print = '''
        --- Post to Print ---
            Post Content to Print
        '''

        with patch('builtins.print') as mocked_print:
            app.print_post(post_to_print)

            mocked_print.assert_called_with(expected_post_print)

    def test_ask_create_post(self):
        with patch('builtins.input') as mocked_input:
            # 3 inputs, we need 3 side effects.
            mocked_input.side_effect = ('Test', 'Test Title', 'Test Content')

            app.ask_create_post()

            self.assertEqual(app.blogs['Test'].posts[0].title, 'Test Title')
            self.assertEqual(app.blogs['Test'].posts[0].content, 'Test Content')