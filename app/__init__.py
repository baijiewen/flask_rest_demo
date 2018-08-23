from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from config import config


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    api1 = Api()
    db.init_app(app)

    from .api_1_0.goods import GoodsAPI
    api1.add_resource(GoodsAPI, '/api/v2.0/goods', endpoint='goods')
    api1.init_app(app)

    from .api_1_0 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')

    return app