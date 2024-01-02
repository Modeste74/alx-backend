#!/usr/bin/env python3
"""defines a sub class LIFOCache"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """inherits from the super and
    defines a caching system"""
    def __init__(self):
        """intializes the class"""
        super().__init__()
        self.last_insert = None

    def put(self, key, item):
        """assigns to dictionary the item value to
        the provided key. Also removes the last data set
        if the capacity is reached"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        # self.last_insert = key
        if len(self.cache_data) > self.MAX_ITEMS:
            discarded_key = self.last_insert
            print(f"DISCARD: {discarded_key}")
            del self.cache_data[discarded_key]
        self.last_insert = key

    def get(self, key):
        """retrieves value associated with key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
