#!/usr/bin/python3
""" Module to start a Flask web application """

from flask import Flask, render_template
from models import storage
app = Flask(__name__, template_folder="templates")


@app.route('/hbnb', strict_slashes=False)
def hbnb_filters():
    """Renders states list into the template "100-hbnb.html"""
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    places = storage.all("Place").values()
    return render_template('100-hbnb.html', states=states, places=places, amenities=amenities)


@app.teardown_appcontext
def close_session(exception):
    """Closes the session after each request"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
