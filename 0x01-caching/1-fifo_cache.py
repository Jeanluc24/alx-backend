#!/usr/bin/env python3
"""
Task 1 - First-In First-Out caching
"""
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Represents object that allows storing and
    retrieves items from dictionary with FIFO
    removal mechanism when limit is reached
    """
    def __init__(self):
        """
        Initializes cache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds item in cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """
        Retrieves item by key
        """
        return self.cache_data.get(key, None)
