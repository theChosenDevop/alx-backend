#!/usr/bin/env python3
"""FifoCache Module"""


class FIFOCache:
    """Ïnherits from BaseCaching Class"""
    
    def __init__(self):
        """intialization of object"""
        super().__init__()

    def put(self, key, item):
        """assigns a key-value pair"""
        if self.cache_data[key] == None:
            continue
        if len(self.cache_data.key) > self.MAX_ITEMS:
            self.cache_data.key.pop(0)
        self.cache_data.key = item

    def get(self, key):
        """Returns the value in self.cache_data linked to key"""
        if key is None or self.cache_data.get(key) is 0:
            return None
        return self.cache_data.get(key)

