#!/usr/bin/env python3
"""FifoCache Module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Ïnherits from BaseCaching Class"""
    def __init__(self):
        """intialization of object"""
        super().__init__()
        self.cache_list = []

    def put(self, key, item):
        """assigns a key-value pair"""
        if key is None or item is None:
            return

        self.cache_data[key] = item
        if key not in self.cache_list:
            self.cache_list.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded = self.cache_list.pop(0)
            print("DISCARD: {}".format(discarded))
            del self.cache_data[discarded]

        #self.cache_data[key] = item

        #if key not in self.cache_list:
        #    self.cache_list.append(key)

    def get(self, key):
        """Returns the value in self.cache_data linked to key"""
        return self.data_cache.get(key, None)
