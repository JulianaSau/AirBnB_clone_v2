#!/usr/bin/python3
""" Module to start a Flask web application """

from flask import Flask
app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    """Returns a string "Hello HBNB!" at the root route"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)