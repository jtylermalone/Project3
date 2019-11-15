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

import os
basedir = os.path.abspath(os.path.dirname(__file__))

# to be completely honest, I have no idea what's going on in this file.
# I know it has something to do with configuring and the database, but
# beyond that I just don't know. I've read the paragraph from the
# tutorial several times but I can't get anything out of it
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False