#!/usr/bin/env python3
"""Redis caching module"""

import redis
import uuid


class Cache:
    """Cache class"""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data) -> any:
        """Store data in cache"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
