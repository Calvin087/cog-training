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
#asd