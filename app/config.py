import os
from dotenv import load_dotenv
# https://flask.palletsprojects.com/en/2.3.x/config/


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_URI_DEV')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY_DEV')


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
