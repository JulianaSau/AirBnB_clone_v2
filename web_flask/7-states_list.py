#!/usr/bin/python3
""" Module to start a Flask web application """

from flask import Flask, render_template
from models import storage
app = Flask(__name__, template_folder="templates")


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Renders “6-number_odd_or_even.html” template only if n is an integer
    """
    states = storage.all("State").values()
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def close_session(exception):
    """Closes the session after each request"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
