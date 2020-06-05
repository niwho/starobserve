# _*_coding:utf-8_*_
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import app
from storage.model.base import db, Base
from storage.model.user import *

# 如果有models文件 一定在上面导入，不然migrates 是识别不到的，就会导入数据库失败

manager = Manager(app=app)

# 添加命令 (数据库相关)
migrate = Migrate(app=app, db=db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
