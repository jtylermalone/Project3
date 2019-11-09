from app import app, db
from app.models import User, Post

# instead of using the python shell in the terminal,
# you can use the flask shell and access the below
# three variables/attributes/whatever you wanna
# call them during that session. According to the
# tutorial, the app.shell_context_processor
# registers and understands this function and registers
# the three items in the return statement.

# NOTE: in order to make this work, you have to set
# FLASK_APP=microblog.py. However, I have a .flaskenv
# in the top level of the microblog directory, and I think
# it handles that automatically so you don't need to
# worry about it.
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
