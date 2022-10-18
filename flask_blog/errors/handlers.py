from flask import Blueprint, render_template
""" In flask you can return a second value in the route
    for the status code, the default is 200 so for custom errors
    we set the error route.
"""

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def error_404(error):
    """ Route to handle 404 error """
    return render_template('errors/404.html'), 404


@errors.app_errorhandler(403)
def error_403(error):
    """ Route to handle 403 error """
    return render_template('errors/403.html'), 403


@errors.app_errorhandler(503)
def error_503(error):
    """ Route to handle 503 error """
    return render_template('errors/503.html'), 503
    
