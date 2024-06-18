import os
from dotenv import load_dotenv
# load_dotenv()
# https://flask.palletsprojects.com/en/2.3.x/config/
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
