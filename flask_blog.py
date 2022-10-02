#!/usr/bin/env python3
from flask import Flask, render_template, url_for, flash, redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
""" This ia the index page equivalent for flask.
    all of the routes are defined here but built inside templates.
    configuration files are set up her and all addition methods are
    like the main app files in React.
"""
app = Flask(__name__)
app.config['SECRET_KEY'] = '4a99b4432d537074f1a38919076236d1'
app.config['SQLALCHEMY_DATDBASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False default='default.jpg')
    password = db.Column(db.String(20), unique=True, nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


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
            return redirect(url_for('home'))
        else:
            flash('Login failed! U tryna hack the page Bru?', 'danger')
    return render_template('login.html', title='Login Bruh', form=form)


if __name__ == '__main__':
    app.run(debug=False)
