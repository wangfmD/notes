# _*_ coding: utf-8 _*_
"""
  __init__.py
  Desc:
  Maintainer: wangfm
  CreateDate: 2016/12/28
"""

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(bootstrap)
    mail.init_app(mail)
    moment.init_app(moment)
    db.init_app(db)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app




