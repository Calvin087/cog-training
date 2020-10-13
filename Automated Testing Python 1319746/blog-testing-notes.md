- [Blog Testing Notes](#blog-testing-notes)
  - [SAVE YOURSELF PAIN](#save-yourself-pain)
  - [Start small and start early.](#start-small-and-start-early)
  - [Unit Tests (posts)](#unit-tests-posts)
    - [Dictionary Checks (useful for REST API's) / JSON-esque](#dictionary-checks-useful-for-rest-apis--json-esque)
  - [The Blog Tests](#the-blog-tests)
  - [Integration test](#integration-test)
  - [TDD](#tdd)
      - [KISS](#kiss)
  - [System Tests](#system-tests)
      - [Testing print() values in console....?](#testing-print-values-in-console)

<br>

# Blog Testing Notes

<br>

## SAVE YOURSELF PAIN
Run these tests from Terminal instead of VSCode.
Add __init__.py files to each folder. For some reason VSCode doesn't like not having these and it complains about imports not working.

```
python3 -m unittest tests/unit/post_test.py
```

Massive problems running the test framework in VSCode, should serve me right relying on this. Need to learn to work more in the Terminal from now on.

<br>

---

<br>

```py

class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

```

Questions to ask when looking at a class to test.

- Q. Does the THING that we want to test, depend only on itself or does it have any other dependencies / files / apis etc?

<br>

---

## Start small and start early.
This code seems small and simple but as the code grows it will no doubt become much more complex.

So test as it grows in complexity, not once it has become a beast.

<br>

---

## Unit Tests (posts)

<br>

**Independence**

For each thing that we want to test that DOESN'T rely on anything else - we treat it as a **unit test**.

Inside the folder for tests, create a folder named ```Unit```.

Blog
- app.py
- blog.py
- post.py
- Tests
  - Unit
    - post_test.py

<br>

**Test Suite**

Each TEST SUITE is a class. eg: post_test.py has a class called PostTest: <-- that's a suite?

A test suite always has to inherit from a TestClass which is ```TestCase```.

The ```TestCase``` class is part of the ```Unit Test``` library.

```
from unittest import TestCase
```

```py

from unittest import TestCase
from post import Post

class PostTest:
    pass

```

All functions that are being tested inside a Class have to start with ```test_``` then the name eg: 

```
def test_create_post
    pass
```

If no errors are raised, we'll get PASS otherwise we'll get FAILURE notifications.

<br>

---

<br>

So I think the test env mimics that this file is in the .Root folder. This is how it imports ```from post import Post```.

It then creates a new Post class/object and passes the title and content as params.

The two tests inside this function check if the title sent over has been assigned to the class correctly, the same with content.

If they have then ```self.title will be title``` otherwise it will fail.

**PASS**

```py

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

# >> --------------------------------
# >> Ran 1 test in 0.000s

# >> OK

```

**FAIL**

```py

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

# Traceback (most recent call last):
#   File "/Users/location/post_test.py", line 15, in test_create_post
#     self.assertEqual("Test Contenido Here", p.content)
# AssertionError: 'Test Contenido Here' != 'Test Content Here'
# - Test Contenido Here
# ?            ^^^
# + Test Content Here
# ?            ^


# --------------------------------
# Ran 1 test in 0.001s

# FAILED (failures=1)


```

### Dictionary Checks (useful for REST API's) / JSON-esque

```asserEqual()``` will check if the dictionary is the same as the dictionary in memory, we don't want to do that. We need to know if the keys and value pairs are matching - ```assertDictEqual(val1, val2)```

```py

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
        # checking if the dictionary's contents are the same.
        # assertEqual only will check if the object is the same
        # in memory, which we don't want.

```

```py

    def test_json(self):
        new_blog = Blog("Test Title", "Test Author")
        new_blog.create_post("Test Post", "Test Content")
        
        expected = {
            'title': 'Test Title',
            'author': 'Test Author',
            'posts': [
                {
                    'title': 'Test Post',
                    'content': 'Test Content'
                }
            ]
        }

        self.assertDictEqual(expected, new_blog.json())

```

<br>

---

## The Blog Tests

<br>

This eventually becomes an in integration test and had to be broken in two because it's no longer only testing one thing. It's reliant on other posts being added - Multiple posts being checked and more.

```py

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

#
# Above this fold we're only looking at unit testing
# --------------------------------------------------
# From here it becomes an integration test.
# I duplicated the file and deleted above and below respectively.
#

    def test_create_post_in_blog(self):
        new_blog = Blog("Test Title", "Test Author")
        new_blog.create_post("Test Post", "Test Content")

        self.assertEqual(len(new_blog.posts), 1)
        self.assertEqual(new_blog.posts[0].title, "Test Post")
        self.assertEqual(new_blog.posts[0].content, "Test Content")

```

<br>

---

## Integration test

<br>

From above this is the snippet for when things became integration

```py

from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):

    def test_create_post_in_blog(self):
        new_blog = Blog("Test Title", "Test Author")
        new_blog.create_post("Test Post", "Test Content")

        self.assertEqual(len(new_blog.posts), 1)
        self.assertEqual(new_blog.posts[0].title, "Test Post")
        self.assertEqual(new_blog.posts[0].content, "Test Content")

    def test_json_no_posts(self):
        new_blog = Blog("Test Title", "Test Author")

        expected = {
            'title': 'Test Title',
            'author': 'Test Author',
            'posts': []
        }

        self.assertDictEqual(expected, new_blog.json())

    def test_json(self):
        new_blog = Blog("Test Title", "Test Author")
        new_blog.create_post("Test Post", "Test Content")
        
        expected = {
            'title': 'Test Title',
            'author': 'Test Author',
            'posts': [
                {
                    'title': 'Test Post',
                    'content': 'Test Content'
                }
            ]
        }

        self.assertDictEqual(expected, new_blog.json())

```

<br>

## TDD

<br>

So TDD is apparently thinking about what you want to test, writing the test and then watching it fail.

Then implementing the simplest version of code to allow the test to pass.....then **rinse and repeat**.

<br>

---

<br>

#### KISS

Write 1 test, fail it, fix it, pass it.

Expand that test.

Write 1 test, fail it, fix it, pass it.

Think of a new test

Write 1 test, fail it, fix it, pass it.

Expand that test

and so on.

<br>

----

<br>

## System Tests

<br>

Different from unit or integration. These tests pass through the entire system.

#### Testing print() values in console....?