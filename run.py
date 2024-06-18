import sqlalchemy as sa
import sqlalchemy.orm as so
from app import create_app, db
from app.models import User
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
# Run the application with the command: .venv/bin/flask run
# source: https://github.com/miguelgrinberg/flasky/issues/332

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User}
