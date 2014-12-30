import functools

class MemoizedFunction(object):
    def __init__(self, func):
        self.__func = func
        self.__cache = {}
        functools.wraps(func)(self)
    def __call__(self, *args, **kwargs):
        frozen_kwargs = tuple(kwargs.iteritems())
        cache_key = args, frozen_kwargs
        if cache_key not in self.__cache:
            self.__cache[cache_key] = self.__func(*args, **kwargs)
        return self.__cache[cache_key]

memoized = MemoizedFunction
__all__ = ['memoized']