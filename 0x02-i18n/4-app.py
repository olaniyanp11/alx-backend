#!/usr/bin/env python3
"""
Basic Flask app
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    a config class to set
    LANGUAGES to ["en","fr"]
    BABEL_DEFAULT_LOCALE to'en'
    BABEL_DEFAULT_TIMEZONE to 'UTC'
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# app.config.from_object(Config)
@app.route('/')
def index():
    """ the index page"""
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """ checkes best conpatible language"""
    locale = request.args.get('locale')
    if locale:
        return request.accept_languages.best_match(['fr'])
    return request.accept_languages.best_match(Config.LANGUAGES)
