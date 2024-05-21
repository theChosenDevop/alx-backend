#!/usr/bin/env python3
"""BaseCache module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Inherits from super BaseCaching"""

    def __init__(self):
        """Initialize instance of a class"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key, None)
