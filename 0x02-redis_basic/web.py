#!/usr/bin/env python3
"""function prototype"""
import requests
from typing import Callable
from functools import wraps
import redis


def cache_page(method: Callable) -> Callable:
    """decorator to count calls of function"""

    @wraps(method)
    def wrapper(url: str) -> str:
        """function to run on the wrapped method"""
        r = redis.Redis()
        r.incr(f"count:{url}")

        page = r.get(f"{url}")
        if page:
            return page.decode("utf-8")
        response = method(url)
        r.set(f"{url}", response, ex=10)
        return response

    return wrapper


@cache_page
def get_page(url: str) -> str:
    """function to get html from url"""
    resonse = requests.get(url)
    return resonse.text
