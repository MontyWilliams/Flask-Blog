#!/usr/bin/env python3
from flask import Flask, render_template, url_for, flash
from forms import RegistrationForm, LoginForm
""" This ia the index page equivalent for flask.
    all of the routes are defined here but built inside templates.
    configuration files are set up her and all addition methods are
    like the main app files in React.
"""
app = Flask(__name__)
app.config['SECRET_KEY'] = '4a99b4432d537074f1a38919076236d1'

posts = [
    {
        'author': 'Monty',
        'title': 'Blog this!',
        'content': 'This is my blog Bro!',
        'date_posted': '100 in the future Bruh'
    },
    {
        'author': 'Twill',
        'title': 'Blog that!',
        'content': 'This is my Bro\'s blog Bro!',
        'date_posted': '100 in the past hommie'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register" , methods=['GET', 'POST'])
def register():
    """ reate instance of RegistrationForm & pass it to the template
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Got you in registered as {form.username.data}!')
    return render_template('registration.html', title='Register Bruh', form=form)


@app.route("/login")
def login():
    """ reate instance of LoginForm & pass it to the template
    """
    form = LoginForm()
    return render_template('login.html', title='Login Bruh', form=form)


if __name__ == '__main__':
    app.run(debug=True)
