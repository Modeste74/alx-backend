#!/usr/bin/env python3
"""defines a sub class"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """inherits from a super class and
    defines a caching system"""
    def __init__(self):
        """initializes the class"""
        super().__init__()
        self.access_tracker = []

    def put(self, key, item):
        """assigns value to the key provided and also
        removes the least recently used key when the cache
        reaches capacity"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if key in self.access_tracker:
            self.access_tracker.remove(key)
        self.access_tracker.append(key)
        if len(self.cache_data) > self.MAX_ITEMS:
            discarded_key = self.access_tracker.pop(0)
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """retrieves value associated with key"""
        if key is None or key not in self.cache_data:
            return None
        self.access_tracker.remove(key)
        self.access_tracker.append(key)
        return self.cache_data[key]
