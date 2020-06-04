# _*_coding:utf-8_*_

from flask import Flask, request
from storage.model.base import db
import settings
from app.hello import hello
from app.user import user
import logging


def register_db(xapp):
    db.init_app(xapp)
    with xapp.app_context():
        db.create_all()


def create_app():
    xapp = Flask(__name__)
    xapp.config.from_object(settings)
    register_db(xapp)
    return xapp


app = create_app()

app.debug = True
handler = logging.FileHandler('starobserve.log')
app.logger.addHandler(handler)
logging.getLogger().addHandler(handler)

app.register_blueprint(hello, url_prefix="/test")
app.register_blueprint(user, url_prefix="/user")
