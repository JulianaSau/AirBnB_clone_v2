#!/usr/bin/python3
""" Module to start a Flask web application """

from flask import Flask, render_template
app = Flask(__name__, template_folder="templates")


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
    """Returns a string "Python " followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Renders “5-number.html” template only if n is an integer"""
    return render_template("5-number.html", number=n)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)