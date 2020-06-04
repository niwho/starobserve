from flask import Blueprint

user = Blueprint('user', __name__, url_prefix='/')

from .views import *
from .db import *

# __all__ = ["user]
