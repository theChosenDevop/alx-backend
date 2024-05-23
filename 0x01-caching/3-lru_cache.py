#!/usr/bin/env python3
"""Least Recent Used Cache module"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """Subclass inherits from superclass BaseCaching"""

    def __init__(self):
        """ïnitialization of instance of a class"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assigns values to keys
           Parameters
                - self: instance of a class
                - key [dict]: key of a dictionary
                - item [dict]: value of the key of a dictionary
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded, _ = self.cache_data.popitem(last=False)
                print("DISCARD: {}".format(discarded))

        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Returns the value linked to key in cache_data object
            Paramters
              - key [dict]: key of a dict
        """
        if key in self.cache_data:
            self.cache_data.move_to_end(key, last=True)
        return self.cache_data.get(key, None)
