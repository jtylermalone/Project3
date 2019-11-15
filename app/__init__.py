# Tyler Malone
# Project 3
# CSCI315
# 11/20/19

# This application was created by following the tutorial found
# at this url:
#
#      https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates
#
# This is a microblog, and as it is now it only consists of a login functionality
# and two "posts" to the blog. Users who are not members of the site can create a
# username and password. User's usernames, passwords, and email addresses are stored in
# a database. I think that's about all there is to this website.

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

############################################
#
# by including this __init__.py file in this
# directory, this directory becomes a package.
# Because it's a package, it can be imported
#
#############################################


app = Flask(__name__)

# the below statement tells flask to use the config file
# in the app folder
app.config.from_object(Config)

# db is an object that represents the database, and
# migrate is an object that represents the migration
# engine
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# initializing flask-login in the ling below
login = LoginManager(app)

# we have to tell flask which view is going to be
# the view handling logins
login.login_view = 'login'

from app import routes, models