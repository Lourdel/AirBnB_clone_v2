#!/usr/bin/python3
"""
script that starts a flas web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """method to display """
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def Hbnb():
    """Display HBNH"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
