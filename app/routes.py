from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


#####################################################################
# export FLASK_DEBUG=1 -> to turn on debug mode

# 404 error - unhandled route

# 500 error - internal server error
#####################################################################


@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Jamal'}
    posts = [
        {
            'author': {'username' : 'DeMarcus'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie isn\'t real cinema!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)