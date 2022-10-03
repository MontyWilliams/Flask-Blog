#!/usr/bin/env python 3
from flask_blog.models import User, Post
from flask_blog import app, db, bcrypt
from flask import render_template, url_for, flash, redirect
from flask_blog.forms import RegistrationForm, LoginForm

""" This is the routing page for the new modular design
"""


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
    """ Create instance of RegistrationForm & pass it to the template
        use bcrypt to generate password hash
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Got you registered as {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('registration.html', title='Register Bruh', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    """ reate instance of LoginForm & pass it to the template
    """
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('Login successful!')
            return redirect(url_for('home'))
        else:
            flash('Login failed! U tryna hack the page Bru?', 'danger')
    return render_template('login.html', title='Login Bruh', form=form)
