#!/usr/bin/env python3
"""cache class"""
import redis
import uuid
from typing import Union, Callable, Optional, Any


class Cache:
    """cache class"""

    def __init__(self):
        """initialized the class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> Any:
        """store method to store data in redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> None:
        """function to get back data from redis"""
        data = self._redis.get(key)
        if not data:
            return

        if fn:
            formatted_data = fn(data)
            return formatted_data
        if fn is int:
            return self.get_int(data)
        if fn in str:
            return self.get_str(data)
        return data

    def get_str(self, data: bytes) -> str:
        return data.decode("utf-8")

    def get_int(self, data: bytes) -> int:
        return int(data)
