
from flask import Flask
from flask_cors import CORS

from config import config
from .utils import populate_config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    populate_config(config[config_name])

    CORS(app, max_age=86400)

    from .main import main as main_blueprint
    # main_blueprint.url_prefix = '/main'
    app.register_blueprint(main_blueprint)

    return app
