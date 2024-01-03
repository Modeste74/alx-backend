#!/usr/bin/env python3
"""defines a subclass MRUCache"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """inherit from the super class and defines
    a caching system"""
    def __init__(self):
        """intializes the class"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """assigns value to key and defines a
        MRU caching system"""
        if key is None or item is None:
            return
        
        if key in self.cache_data:
            del self.cache_data[key]
        elif len(self.cache_data) >= self.MAX_ITEMS:
            discarded_key, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {discarded_key}")
        self.cache_data[key] = item

    def get(self, key):
        """retrieves the value assocaited with key"""
        if key is None or key not in self.cache_data:
            return None
        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return self.cache_data[key]
