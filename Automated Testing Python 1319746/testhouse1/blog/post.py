class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def json(self):
        # basically a python dictionary
        return {
            'title': self.title,
            'content': self.content,
        }

newish_post = Post("hello world", "content")
json = newish_post.json()

print(json["title"])