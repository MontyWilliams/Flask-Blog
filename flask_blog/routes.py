#!/usr/bin/env python 3
from crypt import methods
import secrets
import os
from flask_blog.models import User, Post
from flask_blog import app, db, bcrypt
from flask import render_template, url_for, flash, redirect, request
from flask_blog.forms import RegistrationForm, LoginForm, UpdateAccountForm
from flask_login import login_user, current_user, logout_user, login_required

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
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login failed! U tryna hack the page Bru?', 'danger')
    return render_template('login.html', title='Login Bruh', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext



@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            pass
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Account updated successfully' 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', tittle="Account", image_file=image_file, form=form)
