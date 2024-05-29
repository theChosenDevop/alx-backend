#!/usr/bin/env python3
"""2-app module"""
from flask_babel import Babel, render_template, request
from flask import Flask

app = Flask(__name__)


class Config:
    """Configuration for languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_TIMEZONE = "UTC"


babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Determines the best match with our supported languages"""
    request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', slashes_end=False)
def index():
    """defines index page"""
    title = "Welcome to Holberton"
    render_template("1-index.html", title=title)


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
