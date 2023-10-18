#!/usr/bin/env python3
"""Redis caching module"""

import redis
import uuid
from typing import Union, Callable


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
        data = self.redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data.decode('utf-8') if data is not None else None

    def get_str(self, key: str) -> Union[str, None]:
        """Get string data from cache"""
        return self.get(key)

    def get_int(self, key: str) -> Union[int, None]:
        """Get int data from cache"""
        return self.get(key, fn=int)
