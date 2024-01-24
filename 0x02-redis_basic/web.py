#!/usr/bin/env python3
"""function prototype"""
import requests
from typing import Callable
from functools import wraps
import redis

r = redis.Redis()


def cache_page(method: Callable) -> Callable:
    """decorator to count calls of function"""

    @wraps(method)
    def wrapper(url: str) -> str:
        """function to run on the wrapped method"""

        r.incr(f"count:{url}")

        page = r.get(url)
        if page:
            return page.decode("utf-8")
        response = method(url)
        r.setex(url, 10, response)
        return response

    return wrapper


@cache_page
def get_page(url: str) -> str:
    """function to get html from url"""
    return requests.get(url).text


if __name__ == "__main__":
    get_page("http://slowwly.robertomurray.co.uk")
