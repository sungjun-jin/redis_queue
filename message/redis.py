import redis
import logging

from .exceptions import *

logger = logging.getLogger(__name__)


class RedisQueue():
    def __init__(self):
        self.redis = redis.StrictRedis(
            host="localhost",
            port=6379
        )

        logger.info("redis_initialization")

    def enqueue(self, key, value):
        self.redis.rpush(key, value)

    def dequeue(self, key):
        return self.redis.lpop(key)
