- [Blog Testing Notes](#blog-testing-notes)
  - [SAVE YOURSELF PAIN](#save-yourself-pain)
  - [Start small and start early.](#start-small-and-start-early)
  - [Unit Tests (posts)](#unit-tests-posts)
    - [Dictionary Checks (useful for REST API's) / JSON-esque](#dictionary-checks-useful-for-rest-apis--json-esque)
  - [The Blog Tests](#the-blog-tests)
  - [TDD](#tdd)

<br>

# Blog Testing Notes

<br>

## SAVE YOURSELF PAIN
Run these tests from Terminal instead of VSCode.

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

<br>

---

## The Blog Tests

<br>

```py

from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):

    def test_create_blog(self):
        new_blog = Blog("Test Title", "Test Author")

        self.assertEqual("Test Title", new_blog.title)
        self.assertEqual("Test Author", new_blog.author)
        self.assertListEqual([], new_blog.posts)

```

<br>

## TDD

<br>

So TDD is apparently thinking about what you want to test, writing the test and then watching it fail.

Then implementing the simplest version of code to allow the test to pass.....then **rinse and repeat**.

Posibly write 2 tests, prior to coding up the solution.