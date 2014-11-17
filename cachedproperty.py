#!/usr/bin/env python

from collections import defaultdict

class PropertyCache(object):
    def __init__(self):
        self.has_value = False

    def set(self, value):
        self.value = value
        self.has_value = True

def cachedproperty(method):
    @property
    def cachedproperty_wrapper(self):
        cache = self.property_caches[method]
        if not cache.has_value:
            cache.set(method(self))
        return cache.value
    return cachedproperty_wrapper

class ObjectWithCachedProperties(object):
    def __init__(self):
        self.init_property_caches()

    def init_property_caches(self):
        self.property_caches = defaultdict(PropertyCache)

__all__ = ['cachedproperty', 'ObjectWithCachedProperties']
