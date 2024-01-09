#!/usr/bin/env python3
"""basic flask setup"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _


class Config(object):
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """returns user dict based on id provided"""
    return users.get(user_id)


@app.before_request
def before_request():
    """Executed before all other functions"""
    user_id = request.args.get('login_as')
    user = get_user(int(user_id)) if user_id else None
    g.user = user


@babel.localeselector
def get_locale():
    """determine the best match with our supported languages"""
    user_locale = request.args.get('locale')
    if user_locale and user_locale in app.config['LANGUAGES']:
        return user_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """displays a simple index with some text"""
    if g.user:
        found_user = f"Logged in as {g.user['name']}"
    found_user = _("Not logged in")
    greeting = _('home_header')
    heading = _('home_title')
    return render_template('5-index.html', greeting=greeting,
                           heading=heading, found_user=found_user)


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
