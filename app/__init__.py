import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config


db = SQLAlchemy()


def create_app(config_name):

    # create and configure the app
    app = Flask(__name__)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # load config
    config[config_name].init_app(app, app.instance_path)
    app.config.from_object(config[config_name])

    # load components
    db.init_app(app)

    # load blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .store import store as store_blueprint
    app.register_blueprint(store_blueprint, url_prefix='/store')

    return app
