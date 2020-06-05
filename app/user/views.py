# *_coding:utf-8_*
from . import user
from .db import get_user_from_db
from flask import request, session
import time
from storage.model import UserArticle
from storage.model.base import db
from utils.cache import get_with_cache
from utils import redisClient
import json

USER_NAME = 'user_name'


@user.route('/login', methods=['POST'])
def login():
    user_name = request.form.get('name')
    if not user_name:
        user_name = session.get(USER_NAME)
    if not user_name:
        user_name = "anonymous"

    if user_name != session.get("user_name"):
        session[USER_NAME] = user_name.strip()
    return {'err_code': 0, 'msg': 'success', 'login_name': user_name}


@user.route('/add', methods=['POST'])
def add_user():
    user_name = request.form.get('name')
    email = request.form.get('email')
    print('add_user', user_name, email)
    ua = UserArticle(user_name, email)
    err_code = 0
    msg = "success"
    try:
        db.session.add(ua)
        db.session.commit()
    except Exception as e:
        err_code = 1
        msg = str(e)
    return {'err_code': err_code, 'msg': msg}


@user.route('/del', methods=['POST'])
def del_user():
    user_name = request.form.get('name')
    ua = UserArticle.query.filter_by(username=user_name).first()
    err_code = 0
    msg = "success"
    if ua:
        try:
            db.session.delete(ua)
            db.session.commit()
        except Exception as e:
            err_code = 1
            msg = str(e)
    else:
        err_code = 1
    return {'err_code': err_code, 'msg': msg}


@user.route('/get', methods=['GET'])
def get_user():
    user_name = request.form.get('name')
    info = get_with_cache(lambda: get_user_from_db(user_name), redisClient, key="get_user"+user_name)
    print("info", info, type(info))
    err_code = 0
    msg = "success"
    if not info:
        err_code = 1
        msg = "not found"
    return {
        'err_code': err_code,
        'msg': msg,
        'data': info,
    }


@user.route('/list', methods=['GET'])
def list_user():
    # uas = db.session.query(UserArticle).all()
    uas = UserArticle.query.all()
    err_code = 0
    msg = "success"
    return {
        'err_code': err_code,
        'msg': msg,
        'data': [ua.serialized for ua in uas],
    }
