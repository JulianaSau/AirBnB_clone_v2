#!/usr/bin/python3
""" Module to start a Flask web application """

from flask import Flask, render_template
from models import storage
app = Flask(__name__, template_folder="templates")


@app.route('/states', strict_slashes=False)
@app.route('/states/<string:id>', strict_slashes=False)
def states():
    """Renders states list into the template "9-states.html"""
    states = storage.all("State").values()
    return render_template("9-states.html", states=states)


@app.teardown_appcontext
def close_session(exception):
    """Closes the session after each request"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
