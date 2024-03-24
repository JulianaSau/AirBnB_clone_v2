#!/usr/bin/python3
""" Module to start a Flask web application """

from flask import Flask, render_template
from models import storage
app = Flask(__name__, template_folder="templates")


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Renders states list into the template "8-cities_by_states.html"""
    states = storage.all("State").values()
    print("states", states)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def close_session():
    """Closes the session after each request"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
