from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

# as I've stated elsewhere in comments, Flask makes
# forms really easy. by passing FlaskForm as an
# argument to the class, you just have to follow
# the convention below to define each field. If you
# want to validate the input, you just have to
# include the validators you want (again, as below)
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    # must confirm pw / enter the same pw twice
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    # as it is now, two users cannot have the same username or the same
    # email. When a user is registering, the form submits their potential
    # username and email to be checked against all other usernames and emails
    # that are already in the database. if one of them matches, the user is
    # prompted to enter a different one.
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use  different email address.')