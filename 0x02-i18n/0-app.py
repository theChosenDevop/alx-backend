#!/usr/bin/env python3
"""0-app module"""
from flask import Flask, rebder_template

app = Flask(__name__)


@app.route('/'):
    """routes to the index page"""
    def index():
        title =  “Welcome to Holberton”
        return render_template('template/index.html', title=title)

if __name__ == "__main__":
    app.run(debug=True)
