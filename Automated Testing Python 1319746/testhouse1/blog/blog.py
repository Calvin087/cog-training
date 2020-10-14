from post import Post

class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        p_plural = 's' if len(self.posts) != 1 else ''

        return f"{self.title} by {self.author} ({len(self.posts)} post{p_plural})"

    def create_post(self, title, content):
        self.posts.append(Post(title, content))
        # not receiving a object, so we have to create it.

    def json(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': [post.json() for post in self.posts],
            # posts is an integration method, so a test is needed for that
        }

        