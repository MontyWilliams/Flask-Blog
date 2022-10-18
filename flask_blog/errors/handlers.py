from flask import Blueprint

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def error_404(error):
    """ Route to handle 404 error"""
    return render_template('errors.404.html')
