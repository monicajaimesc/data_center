#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """returns everithin is cool"""
    return 'the coolest!'

@app.route('/number_template/<int:n>', strict_slashes=False)
def numbersandtemplates(n):
    """display a HTML page only if n is an integer"""
    return render_template('number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')