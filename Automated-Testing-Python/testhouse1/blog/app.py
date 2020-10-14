from blog import Blog

MENU_PROMPT = "Enter 'c' to create a blog, 'l' to list blogs, 'r' to read one, 'p' to create a post, or 'q' to quit: " 

POST_TEMPLATE = '''
        --- {} ---
            {}
        '''

blogs = dict()

def menu():
    print_blogs()
    selection = input(MENU_PROMPT)
    
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)

def print_blogs():
    for key, post in blogs.items():
        print(f"- {post}")

def ask_create_blog():
    title = input('Enter a blog Title: ')
    author = input('Enter your name: ')

    blogs[title] = Blog(title, author)
    # print(blogs)

def ask_read_blog():
    title = input('Enter a blog title you want to read: ')
    print_posts(blogs[title])

def print_posts(blog):
    for post in blog.posts:
        print_post(post)

def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))

def ask_create_post():
    blog_name = input("Enter name of blog you're writing for: ")
    title = input("What's the title of your post: ")
    content = input("write something epic: ")

    # Retrieve blog / create post <-- (function from blog.py)
    blogs[blog_name].create_post(title, content)
