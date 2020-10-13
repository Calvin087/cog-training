[Check against this](https://github.com/schoolofcode-me/testing-python-apps/tree/master/section3/video_code)

<br>

# Blog Testing Notes

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

## Unit Tests

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