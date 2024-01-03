#!/usr/bin/env python3
"""defines a subclass LFUCache"""
from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """inherits from super and defines a caching system"""
    def __init__(self):
        """initializes the class"""
        super().__init__()
        self.cache_data = {}
        self.frequency = defaultdict(int)
        self.usage_order = OrderedDict()

    def put(self, key, item):
        """assigns the value to the key provided.
        Also defines a LFU caching system to deal with
        the capicty of the cahce"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.usage_order.move_to_end(key)
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                self.remove_lfu()

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage_order[key] = None

    def get(self, key):
        """retrieves value associated with key whilst
        also update the frequency in"""
        if key is None or key not in self.cache_data:
            return None
        self.frequency[key] += 1
        self.usage_order.move_to_end(key)
        return self.cache_data[key]

    def remove_lfu(self):
        """discards the data with the least frequency of usage
        from the caching system"""
        min_freq = min(self.frequency.values())
        min_f = [k for k, v in self.frequency.items() if v == min_freq]
        if len(min_f) > 1:
            for key in self.usage_order:
                if key in min_f:
                    del self.cache_data[key]
                    del self.frequency[key]
                    del self.usage_order[key]
                    print(f"DISCARD: {key}")
                    break
        else:
            key_to_remove = min_f[0]
            del self.cache_data[key_to_remove]
            del self.frequency[key_to_remove]
            del self.usage_order[key_to_remove]
            print(f"DISCARD: {key_to_remove}")
