MENU_PROMPT = "Enter 'c' to create a blog, 'l' to list blogs, 'r' to read one, 'p' to create a post, or 'q' to quit: " 

blogs = dict()

def menu():
    print_blog_posts()
    selection = input(MENU_PROMPT)

def print_blog_posts():
    for key, post in blogs.items():
        print(f"- {post}")
