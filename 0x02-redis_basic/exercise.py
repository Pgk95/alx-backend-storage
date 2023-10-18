#!/usr/bin/env python3
"""Redis caching module"""

import sys
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Count calls decorator"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        self._redis.INCR(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """Cache class"""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in cache"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable[[bytes],
                                         Union[str, int, None]]
            = None) -> Union[str, int, None]:
        """Get data from cache"""
        if fn:
            return fn(self._redis.get(key))
        data = self._redis.get(key)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """Get string data from cache"""
        return self.get(key)

    def get_int(self, key: str) -> Union[int, None]:
        """Get int data from cache"""
        return self.get(key, fn=int)
