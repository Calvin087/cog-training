
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

## 

<br>