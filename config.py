import os
# from dotenv import load_dotenv
# load_dotenv()
# https://flask.palletsprojects.com/en/2.3.x/config/
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
