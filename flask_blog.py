#!/usr/bin/env python3
from flask import Flask, render_template, url_for, flash, redirect
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


@app.route("/register", methods=['GET', 'POST'])
def register():
    """ reate instance of RegistrationForm & pass it to the template
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Got you registered as {form.username.data}!', 'sucess')
        return redirect(url_for('home'))
    return render_template('registration.html', title='Register Bruh', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    """ reate instance of LoginForm & pass it to the template
    """
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('Login successful!')
            return redirect(url_fot('home'))
    return render_template('login.html', title='Login Bruh', form=form)


if __name__ == '__main__':
    app.run(debug=False)
