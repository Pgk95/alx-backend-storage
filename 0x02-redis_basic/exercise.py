#!/usr/bin/env python3
"""Redis caching module"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Counts call decorator"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = "{}:inputs".format(method.__qualname__)
        output_key = "{}:outputs".format(method.__qualname__)
        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))
        return result
    return wrapper


def replay(func):
    """Replay decorator"""
    qualified_name = func.__qualname__
    inputs_key = f"{qualified_name}:inputs"
    outputs_key = f"{qualified_name}:outputs"

    inputs = [input.decode('utf-8')
              for input in Cache._redis.lrange(inputs_key, 0, -1)]
    outputs = [output.decode('utf-8')
               for output in Cache._redis.lrange(outputs_key, 0, -1)]

    print(f"{qualified_name} was called {len(inputs)} times:")
    for input_data, output_data in zip(inputs, outputs):
        print(f"{qualified_name}(*({input_data},)) -> {output_data}")


class Cache:
    """Cache class"""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in cache"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable[[bytes],
                                         Union[str, int, None]]
            = lambda data: data) -> Union[str, int, None]:
        """Get data from cache"""
        data = self._redis.get(key)
        return fn(data)

    def get_str(self, key: str) -> Union[str, None]:
        """Get string data from cache"""
        return self.get(key)

    def get_int(self, key: str) -> Union[int, None]:
        """Get int data from cache"""
        return self.get(key, fn=int)
