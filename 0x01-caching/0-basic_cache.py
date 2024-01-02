#!/usr/bin/env python3
"""defines a sub class BasicCache"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Inherits from the super BaseCaching"""
    def __init__(self):
        """Intializes the class with super"""
        super().__init__()

    def put(self, key, item):
        """assigns to dictionary item value
        for the key provided"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """returns value in self.cache_data linked
        to the key provided"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
