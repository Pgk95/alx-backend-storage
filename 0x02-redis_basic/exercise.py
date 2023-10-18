#!/usr/bin/env python3
"""Redis caching module"""

import redis
import uuid


class Cache:
    """Cache class"""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data) -> [str, bytes, int, float]:
        """Store data in cache"""
        key = str(uuid.UUID())
        self._redis.set(key, data)
        return key
