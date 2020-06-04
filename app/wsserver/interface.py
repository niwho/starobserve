# _*_coding:utf-8_*_

# 以下接口的实现不能用local的，redis+db


def get_user_rooms(uid):
    """
    返回用户的会话/房间列表
    db+cache存储，全局访问

    """
    pass


def join_room(uid, room_id):
    """
    用户加入房间或会话，房间是否必须先创建？ 私人会话随意，多人群聊需要权限
    :param uid:
    :param room_id:
    :return:
    """
    pass


def left_room(uid, room_id):
    """
    :param uid:
    :param room_id:
    :return:
    """
    pass


def get_room_users(room_id):
    """
    获取房间里的所有用户，冷启动接口
    实时消息是广播到每个实例，发送在线用户
    :param room_id:
    :return:
    """
    pass


def get_room_current_node_users(room_id):
    """
    获取当前节点的在线用户
    :param room_id:
    :return:
    """
    pass


def get_room_msg_history(room_id, less_than_id, time_stamp, limit=10):
    """
    获取房间聊天记录
    :param room_id: 房间id
    :param less_than_id: 消息id， -1 表示无效
    :param time_stamp: 时间戳，指定了消息id（非-1）时间戳无效， unix时间
    :param limit: 条数
    :return: true 还有更多记录， false 没有
    """
    pass


# 消息id， 房间id， 用户id，的生成，基于数据从1开始的递增方案
def generate_id(type):
    """

    :param type: 类型 0用户id，1房间id， 3，消息id
    :return: 长整数
    """
    pass