#!/usr/bin/python3
"""
this is module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    this is a class
    """
    def put(self, key, item):
        """ this ,is a method
        """
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """
        this is a method
        """
        return self.cache_data.get(key, None)
