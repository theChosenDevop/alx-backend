#!/usr/bin/env python3
"""2-app module"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """Configuration for languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Determines the best match with our supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', slashes_end=False)
def index() -> str:
    """defines index page"""
    title = "Welcome to Holberton"
    return render_template("2-index.html", title=title)


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
