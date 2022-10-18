from flask_blog import db, login_manager, app
from datetime import datetime
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
""" These are all the models used in the db
    - The serializer is used to handle password
    - Date time is used tko add time stamps to posts
    - login_manager privides user session management for Flask
"""

@login_manager.user_loader
def load_user (user_id):
    """ the module stores user id's in session and reminds me of reacts
        state and context management
    """
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """ User db model for users in the app
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(20), unique=True, nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        """ Reset token using serialization for hanldling secure password
            they will have 30 mins to reset their password
        """
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf8')

    @staticmethod
    def verify_reset_token(token):
        """ verify token by trying to mimic values
            - Tries to get user_id to verify that serialization is correct
            - handles fail case
            - because it dosent use the anything from its class 
        """
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

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
