#!/usr/bin/python3
"""
script that starts a flas web application
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """method to display """
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def Hbnb():
    """Display HBNH"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_route(text):
    """display “C ” followed by the value of the text variable"""
    return ("C " + text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pyiscool(text="is cool"):
    """
    display “Python ”, followed by the value of the text variable
    """
    return ("Python " + text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def Number(n):
    """
    display “n is a number” only if n is an integer
    """
    return f"{n} is a number\n"


@app.route("/number_template/<int:n>", strict_slashes=False)
def Number_temp(n):
    """
    display a HTML page only if n is an integer
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def Number_odd_or_even(n):
    """
    display a HTML page only if n is an integer
    """
    if (n % 2 != 0):
        number = "odd"
    else:
        number = "even"
    return render_template("6-number_odd_or_even.html", n=n, number=number)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
