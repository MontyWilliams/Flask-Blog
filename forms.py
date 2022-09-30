from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length, Email
""" This module provides our app with forms
    the syntax will be diff than regular html
    as it uses flask_wtf's methods
"""


class RegistrationForm(FlaskForm):
    """ The fields will all be methods
    """
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
