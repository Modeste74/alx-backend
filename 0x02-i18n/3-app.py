#!/usr/bin/env python3
"""basic flask setup"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config(object):
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """determine the best match with our supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """displays a simple index with some text"""
    greeting = _('home_header')
    heading = _('home_title')
    return render_template('1-index.html', greeting=greeting, heading=heading)


if __name__ == '__main__':
    app.run(debug=True)
