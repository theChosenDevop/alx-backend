#!/usr/bin/env python3
"""0-app module"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """routes to the index page"""
    title = "Welcome to Holberton"
    return render_template('template/index.html', title=title)

if __name__ == "__main__":
    app.run(debug=True)
