import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config


bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):

    # create and configure the app
    app = Flask(__name__)

    # load config
    config[config_name].init_app(app, app.instance_path)
    app.config.from_object(config[config_name])

    # load components
    bootstrap.init_app(app)
    db.init_app(app)
    migrate = Migrate(app, db)

    # load blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .store import store as store_blueprint
    app.register_blueprint(store_blueprint, url_prefix='/store')

    return app
