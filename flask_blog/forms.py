from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
""" This module provides our app with forms
    the syntax will be diff than regular html
    as it uses flask_wtf's methods.
    Module never accesses anything outside of itself
"""


class RegistrationForm(FlaskForm):
    """ This class provides all the functionality needed to register
        in th Db. all methods are implementations of the wtforma package 
        which comes with FlaskForm
    """
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                           validators=[DataRequired(), Length(min=2, max=20)])
    confirm_password = PasswordField('Confirm Password',
                           validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Signup')    

class LoginForm(FlaskForm):
    """ Similar to the RegistrationForm bu used for login instead
    """
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                           validators=[DataRequired(), Length(min=2, max=20)])
    remember = BooleanField('Remember Me')
    
    submit = SubmitField('Signup')
