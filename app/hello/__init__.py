from flask import Blueprint

hello = Blueprint('hello', __name__, url_prefix='/')

from .views import index