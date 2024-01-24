#!/usr/bin/env python3
"""cache class"""
import redis
import uuid
from typing import Union, Callable, Optional, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """decorator to count calls of function"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """function to run on the wrapped method"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """decorator to store inputs and outputs"""
    input_key = method.__qualname__ + ":inputs"
    output_key = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """function to run on the wrapped method"""

        self._redis.rpush(input_key, str(args))
        result = method(self, *args)
        self._redis.rpush(output_key, result)
        return result

    return wrapper


class Cache:
    """cache class"""

    def __init__(self):
        """initialized the class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store method to store data in redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """function to get back data from redis"""
        data = self._redis.get(key)
        if not data:
            return

        if fn:
            formatted_data = fn(data)
            return formatted_data
        if fn is int:
            return self.get_int(data)
        if fn is str:
            return self.get_str(data)
        return data

    def get_str(self, data: bytes) -> str:
        return data.decode("utf-8")

    def get_int(self, data: bytes) -> int:
        return int(data)
