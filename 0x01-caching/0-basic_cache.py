#!/usr/bin/env python3
"""
Task 0 - Basic caching
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Represents object that allows storing and
    retrieves items from dictionary
    """
    def put(self, key, item):
        """
        Adds item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves item by key
        """
        return self.cache_data.get(key, None)
