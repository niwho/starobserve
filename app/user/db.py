# encoding=utf8
from storage.model import UserArticle


def get_user_from_db(user_name):
    ua = UserArticle.query.filter_by(username=user_name).first()
    return ua
