
# Flask Testing Notes

<br>

## Environment

<br>

Refer to the old set up notes for unittesting.

Create a new file for ```requirements.txt```, add Flask and save.

#### Installing Flask

Not sure if i'm supposed to install flask in the venv or in the root folder. I inititally went for the venv, not sure how that's going to work out.

Using Python3+ the install should be

```
pip3 install flask
```

**eg:**

```
 python3 -m unittest tests/system/home_test.py
```

Placing it in the ```venv``` worked.

---

<br>

## Importing Flask

<br>

Our tests are going to import ```app``` so they have access to our app. If another file imports app we don't want app to run.

<br>

> **Issue with Tutoring sessions**

<br>

The modules we import during tutoring always seem to run the entire import. This is probably why. I guess python is treating all files independently. With ```__main__``` - It might allow us to get around that issue.

```py

from flask import Flask, jsonify

app = Flask(__name__)
# flask object __ is unique name identifier 

@app.route('/')
# "End Point" basically http://www.xyz.com/

def home():
    return  jsonify({'message': 'Hello World'})
    # Flask can not have an end point return dictionaries. STR yes.
    # so we have to import jsonify for it to work.
    # converts the dictionary into a string.

if __name__ == '__main__':
    app.run()

    # if __name__ This has to do with the way Py imports modules.
    # It looks like it just decides that this is the 
    # highest parent in the structure while importing others.


# > {
# >     "message": "Hello World"
# > }

```

Test example. ```test_client()``` comes from Flask.

```py

from unittest import TestCase
from app import app

class TestHome(TestCase):
    def test_home(self):
        with app.test_client() as c:
            response = c.get('/')

        # Test client comes from Flask
        # Doesn't run everything in the bg
        # making a request to the app

            self.assertEqual(response.status_code, 200)

            

```

---

<br>

## Base Test?

<br>

This one has to have a different pattern from the other test files because it's not going to include any test methods.

My files are usually X_test

```
base_test.py
```
After creating that file, I've now imported and changed over the parent parameter in ```home_test.py```. Also changing the Parent class param to ```BaseTest``` as it's no longer being pulled from ```unittest```.

All global changes that I want to make to the test suite now only really have to be made inside BaseTest from now on, with some careful considerations.

**Home_test.py**

```py

from tests.system.test_base import BaseTest
import json

class TestHome(BaseTest):
    def test_home(self):
        with self.app() as c:
        # self.app is being pulled from based test where we're
        # initiating app.test_client
            response = c.get('/')

        # Test client comes from Flask
        # Doesn't run everything in the bg
        # making a request to the app

            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                json.loads(response.get_data()),
                {'message': 'Hello World'}
            )
            # Load S means load string, not loads plural.
            # This turns our dictionary into a json string from app.py.

```

**Test_base.py**

```py

from unittest import TestCase
from app import app

class BaseTest(TestCase):
    def setUp(self):
        # this runs before each test.
        self.app = app.test_client

```