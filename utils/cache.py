# encoding=utf8
import logging
import json
from storage.model.base import AlchemyEncoder

TTL = 60*5
EMPTY = 15

def get_with_cache(func, cache, key):
    try:
        val = cache.get(key)
        print("cache", val)
        if val:
            return json.loads(val)
        if func:
            val = func()

            print("db", val)
            if val:
                cache.set(key, str(val), TTL)
            return val.serialized
    except Exception as e:
        cache.set(key, "{}", EMPTY)
        # from app import app
        # app.logger.error("error:{}, key:{}".format(e, key))
        logging.getLogger().error("error:{}, key:{}".format(e, key))
        return

