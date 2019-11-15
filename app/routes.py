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

from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse


#####################################################################
# export FLASK_DEBUG=1 -> to turn on debug mode

# 404 error - unhandled route

# 500 error - internal server error
#####################################################################

# all routes are defined below

# this route is the default/index route. it is reached if the user
# tries localhost:5000 or localhost:5000/ or localhost:5000/index
@app.route('/')
@app.route('/index')
# @login_required makes the user be logged in before they can
# view the content of the page
@login_required
def index():

    # these are the posts that are going to be displayed on the
    # index page. there are only two right now and I copied them
    # from the tutorial (for the most part)
    posts = [
        {
            'author': {'username' : 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie isn\'t real cinema!'
        }
    ]

    # render_template must be imported from flask at the top
    return render_template('index.html', title='Home', posts=posts)

# this route is the login page. since the page receives inromation
# from a form, it has to be accessible by both get and post methods,
# hence why both are explicitly stated below
@app.route('/login', methods=['GET', 'POST'])
def login():
    # if the user is logged in, they are just taken straight to the
    # index page
    if current_user.is_authenticated:

        # you must import redirect from flask at the top
        return redirect(url_for('index'))

    # WTForms makes forms very easy. LoginForm() is defined in the forms.py
    # file. refer to that file for more information on how the form is
    # structured. here, the form variable is populated with a LoginForm
    # and in the bottom return statement, the form variable is passed
    # to the login view.
    form = LoginForm()

    # validate_on_submit returns true if the browser sends a POST
    # request.
    if form.validate_on_submit():

        # here, the database is queried to find the user with the username
        # that matches the username that was input by the user into the
        # login form. if there isn't a match in the database, or if the
        # password doesn't match the relevant password from the database,
        # the user is told so and redirected to the login page.
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            # you must import redirect from flask at the top
            return redirect(url_for('login'))

        # all that's needed to log the user in is the statement
        # below. flask_login takes care of everything and makes it
        # easy on us. if the user checks the "remember me" box,
        # they won't have to login again next time (this is obvious)
        login_user(user, remember=form.remember_me.data)

        # the request may include information about what page
        # to go to next. this info is stored in the 'next' variable
        # in the request. if there isn't a specified next page,
        # the user is taken back to the index page
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')

        # you must import redirect from flask at the top
        return redirect(next_page)

    # render_template must be imported from flask at the top
    return render_template('login.html', title='Sign In', form=form)

# logout route... pretty simple. flask_login has a logout_user()
# command that does what it says. when the user logs out they are taken
# back to the index page, where they will be asked to log back in
@app.route('/logout')
def logout():
    logout_user()
    # you must import redirect from flask at the top
    return redirect(url_for('index'))

# whenever the user wants to register an account. since this page
# receives information from a form, it has to be accessible by both
# get and post methods, hence why both are explicitly stated below
@app.route('/register', methods=['GET', 'POST'])
def register():

    # if the user is logged in, they are taken back to the index
    # page
    if current_user.is_authenticated:

        # you must import redirect from flask at the top
        return redirect(url_for('index'))

    # WTForms makes forms really easy for us. Here, the form variable is
    # populated with an instance of a RegistrationForm()... this form
    # is defined in the forms.py file... refer to that file for more information
    # on the form
    form = RegistrationForm()

    # this stuff below actually adds the new user and his/her info to
    # the database if the form data is all valid
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)

        # we never see the user's password
        user.set_password(form.password.data)

        # adding the user only readies the user to be put into
        # the database, it doesn't actually add anything to the
        # database yet
        db.session.add(user)

        # you must commit() the data to the database in order for it
        # to be actually stored in there
        db.session.commit()
        flash('Congratulations, you are now a registered user!')

        # you must import redirect from flask at the top
        return redirect(url_for('login'))

    # you must import render_template from flask at the top
    return render_template('register.html', title='Register', form=form)