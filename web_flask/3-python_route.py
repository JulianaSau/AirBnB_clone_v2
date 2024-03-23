#!/usr/bin/python3
""" Module to start a Flask web application """

from flask import Flask
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello():
    """Returns a string "Hello HBNB!" at the root route"""
    return "Hello HBNB!"


@app.route('/hbnb', methods=['GET'], strict_slashes=False)
def hbnb():
    """Returns a string "HBNB" at the /hbnb route"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Returns a string "C " followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """Returns a string "C " followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)