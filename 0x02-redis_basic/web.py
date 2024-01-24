#!/usr/bin/env python3
"""function prototype"""
import requests
from typing import Callable
from functools import wraps
import redis


def count_calls(method: Callable) -> Callable:
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
        r.set(f"{url}", response, 10)
        return response

    return wrapper


@count_calls
def get_page(url: str) -> str:
    """function to get html from url"""
    return requests.get(url).text


get_page("https://www.google.com")
