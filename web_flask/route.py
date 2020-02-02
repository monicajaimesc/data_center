#!/usr/bin/python3
"""
script that starts a Flask web application
"""""

from flask import Flask

app = Flask(__name__)


# specify URL

@app.route("/", strict_slashes=False)


def Hello_route():
    # what that URL returns
    return "Hello HBNB!"

# @app.route("/number/", defaults={"n": 'is a number'})
@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    web application

    :param n is an integer:
    :return: display a number
    """
    return "{:d} is a number".format(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    web application number five
    :return: display a HTML page only if n is an integer
    """
    # Flask will look for templates in the templates folder.
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run()