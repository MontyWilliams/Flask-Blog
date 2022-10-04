#!/usr/bin/env python 3
from flask_blog.models import User, Post
from flask_blog import app, db, bcrypt
from flask import render_template, url_for, flash, redirect
from flask_blog.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user

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
    if current_user.is_authenticated:
        flash('You are already registered Bruh bruh', 'danger')
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created, U may login now!', 'success')
        return redirect(url_for('login'))
    return render_template('registration.html', title='Register Bruh', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    """ reate instance of LoginForm & pass it to the template
    """
    if current_user.is_authenticated:
        flash('You already logged in Hommie', 'danger')
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login failed! U tryna hack the page Bru?', 'danger')
    return render_template('login.html', title='Login Bruh', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
