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

from app import app, db
from app.models import User, Post

# instead of using the python shell in the terminal,
# you can use the flask shell and access the below
# three variables/attributes/whatever you wanna
# call them during that session. According to the
# tutorial, the app.shell_context_processor
# registers and understands this function and registers
# the three items in the return statement.

# to enter the flask shell, navigate to the microblog
# top level directory and enter this command into
# the terminal:
#
#           flask shell
#
# ... it's that simple. you can create new users, edit
# user info, etc from the flask shell

# NOTE: in order to make this work, you have to set
# FLASK_APP=microblog.py. However, I have a .flaskenv
# in the top level of the microblog directory, and I think
# it's handling that automatically so you don't need to
# worry about it.
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
