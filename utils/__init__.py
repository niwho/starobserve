# encoding=utf8

import redis
import settings


pool = redis.ConnectionPool(host=settings.REDIS_CONF['host'],
                            port=settings.REDIS_CONF['port'],
                            db=settings.REDIS_CONF['db'])
redisClient = redis.Redis(connection_pool=pool)
