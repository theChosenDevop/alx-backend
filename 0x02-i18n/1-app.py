#!/usr/bin/env python3
"""1-app module"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """Configuration for langauges"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index() -> str:
    """routes to the index page"""
    title = "Welcome to Holberton"
    return render_template("0-index.html", title=title)


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
