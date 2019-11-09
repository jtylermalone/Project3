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