# _*_coding:utf-8_*_
from storage.model.base import Base, db
import json
from .base import AlchemyEncoder


class UserArticle(Base):

    __tablename__ = 'article_user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

    @property
    def serialized(self):
        """Return object data in serializeable format"""
        from sqlalchemy.orm import class_mapper
        columns = [c.key for c in class_mapper(self.__class__).columns]
        return dict((c, getattr(self, c)) for c in columns)

    def __str__(self):
        return json.dumps(self.serialized)
