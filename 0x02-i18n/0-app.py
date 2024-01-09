#!/usr/bin/env python3
"""basic flask setup"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """displays a simple index with some text"""
    greeting = "Hello world"
    heading = "Welcome to Holberton"
    return render_template('1-index.html', greeting=greeting, heading=heading)


if __name__ == '__main__':
    app.run(debug=True)
