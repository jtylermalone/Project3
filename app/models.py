from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# this file defines the tables in the database.
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# UserMixin includes "generic implementations" (methods) that are relevant
# to most models. By including UserMixin as an argument in the
# User class, you can use all of the UserMixin methods on items
# in the table

# All of the columns in the User table are defined within the
# class. I think it's pretty obvious/simple what's going on except
# for with the posts variable
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    # this statement creates a one-to-many relationship between
    # users and posts. The first argument is the table being referenced,
    # The backref='author' statement creates a reference for each post
    # that will provide the author of that post. For example, to get
    # the author of a post, you would just use post.author. I don't know
    # what the lazy='dynamic' part means, I just followed the tutorial for
    # that.
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    # the __repr__ method determines how a user instance is printed
    # to the console. It's a lot like a toString method in java.
    def __repr__(self):
        return '<User {}>'.format(self.username)

    # as the developer of the site, you never see users' actual passwords.
    # instead, the passwords pass through werkzeug's password hashing
    # function, which is unreversable according to the tutorial.
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # this function is used when a user logs in. if the inputted password's
    # hash matches that of the hash of the password in the database, then
    # you can be sure that it's the right password
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# much like the User table above, each of the columns in the posts
# table is defined in the class, as well as a __repr__ method
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # the __repr__ method determines how a user instance is printed
    # to the console. It's a lot like a toString method in java.
    def __repr__(self):
        return '<Post {}>'.format(self.body)