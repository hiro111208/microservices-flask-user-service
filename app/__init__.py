from flask import Flask
from config import DevelopmentConfig

# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-a-better-application-structure


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    with app.app_context():
        # Register blueprints
        from .user_api import user_api_blueprint
        app.register_blueprint(user_api_blueprint, url_prefix='/user-api')
        return app
