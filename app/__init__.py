from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_mail import Mail
from config import config
from celery import Celery


db = SQLAlchemy()
celery = Celery()
mail = Mail()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    api1 = Api()
    db.init_app(app)

    celery.__init__(app.name, broker=app.config['CELERY_BROKER_URL'])
    # # celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
    # print app.name
    celery.conf.update(app.config)
    # print celery._preconf['BROKER_URL']
    mail.init_app(app)

    from .api_1_0.goods import GoodsAPI
    api1.add_resource(GoodsAPI, '/api/v2.0/goods', endpoint='goods')
    api1.init_app(app)

    from .api_1_0 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
