#!/usr/bin/env python3
"""
Writing strings to redis
"""

import redis
from typing import Union, Callable, Optional
import uuid


class Cache:
    """
    class cache
    """
    def __init__(self) -> None:
        """
        initialise redis instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        generate a rendom key
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[bytes, str, int, float]:
        """
        converts data back to desired format
        """
        value = self._redis.get(key)
        if not fn:
            return value
        return fn(value)

    def det_str(self, key) -> str:
        str_value = self._redis.get(key)
        return str_value.decode('utf-8')
