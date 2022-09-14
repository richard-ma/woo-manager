import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config


db = SQLAlchemy()


def create_app(config_name):

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # load config
    app.config.from_object(config[config_name])
    config[config_name].init_app(app, app.instance_path)

    # load components
    db.init_app(app)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
