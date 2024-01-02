#!/usr/bin/env python3
"""defines a sub class FIFOCache"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """The following inherits from super class to
    implement a caching system"""
    def __init__(self):
        """Intializes the class"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """assigns to dictionary the item value
        for the key provided. It also discards
        the first item if the max items is reached and
        data is being added to the cache"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            discarded_key = self.queue.pop(0)
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")
        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """return the value associated
        with the provided key"""
        if key is None or self.cache_data[key] is None:
            return None
        return self.cache_data[key]
