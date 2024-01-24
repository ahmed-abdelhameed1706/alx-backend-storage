#!/usr/bin/env python3
"""cache class"""
import redis
import uuid
from typing import Union


class Cache:
    """cache class"""

    def __init__(self):
        """initialized the class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store method to store data in redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
