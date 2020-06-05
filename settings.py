
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123@127.0.0.1:3306/book1'
#postgresql+pg8000://scott:tiger@localhost/test
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:mysecrt@192.168.31.29:5432/db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

REDIS_CONF = {
    'host': "",
    'port': 6379,
    'db': 0,
}

# cookies配置
SECRET_KEY = 'jkdfkldsjdfkai134^&5'

from loacal_config import *