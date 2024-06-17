from . import user_api_blueprint


@user_api_blueprint.route('/')
def index():
    return 'Hello, World!'
