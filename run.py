#!/usr/bin/env python 3
from flask_blog import app
""" This file is used to run the app
    It imprts based on the contents of __init__
    file which contains the app
"""

if __name__ == '__main__':
    app.run(debug=True)
