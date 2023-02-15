#!/usr/bin/env python3
"""
Writing strings to redis
"""

import redis
from typing import Union
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
