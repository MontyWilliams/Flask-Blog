from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_blog.models import User
from flask_login import current_user



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

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username already in use Bruh!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already in use Bruh Bruh') 

class LoginForm(FlaskForm):
    """ Similar to the RegistrationForm but used for login instead
    """
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                           validators=[DataRequired(), Length(min=2, max=20)])
    remember = BooleanField('Remember Me')
    
    submit = SubmitField('Signup')

class UpdateAccountForm(FlaskForm):
    """ This class provides all the functionality needed to update 
        the user account settings
    """
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Change Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username already in use Bruh!')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is already in use Bruh Bruh')
                


class RequestResetForm(FlaskForm):
    """ form for changing password
    """
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('Email dont exist bru') 


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password',
                           validators=[DataRequired(), Length(min=2, max=20)])
    confirm_password = PasswordField('Confirm Password',
                           validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')
