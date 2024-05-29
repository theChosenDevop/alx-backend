#!/usr/bin/env python3
"""0-app module"""
from flask import Flask, rebder_template


app = Flask(__name__)

@app.route('/'):
    def index():
        return render_template('template/index.html')
