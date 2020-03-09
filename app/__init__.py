# app/__init__.py

from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

import os

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the config file
app.config.from_object('config')



# Load the views
from app import views
from app import models
from app.models import db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


# Setting Secret Key
app.secret_key = os.urandom(12)

if __name__ == '__main__':
    app.run(debug=True)