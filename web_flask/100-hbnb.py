#!/usr/bin/python3
"""Start a Flask web app"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.place import Place
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """removes  SQLAlchemy Session"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb_filters():
    """Displays HBnB page"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
