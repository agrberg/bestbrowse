import functools
import json
import pickle
import inspect
import os.path
import persistence

class MemoizedFunction(object):
    def __init__(self, func):
        self.__func = func
        self._cache = {}
        functools.wraps(func)(self)
    def __call__(self, *args, **kwargs):
        frozen_kwargs = tuple(kwargs.iteritems())
        cache_key = args, frozen_kwargs
        if cache_key not in self._cache:
            self._cache[cache_key] = self.__func(*args, **kwargs)
        return self._cache[cache_key]

class PersistentDictionary(object):
    def __init__(self, file_path):
        self.__file_path = file_path
        if os.path.exists(file_path):
            with open(file_path, 'r') as ifile:
                self.__dict = pickle.load(ifile)
        else:
            self.__dict = {}

    def __getitem__(self, key):
        return self.__dict[key]

    def __setitem__(self, key, value):
        self.__dict[key] = value
        with open(self.__file_path, 'w') as ofile:
            pickle.dump(self.__dict, ofile)

    def __contains__(self, key):
        return key in self.__dict

    def __iter__(self):
        return iter(self.__dict)

    def __getattr__(self, attribute_name):
        return getattr(vars(self)['_PersistentDictionary__dict'], attribute_name)

class PersistentlyMemoizedFunction(MemoizedFunction):
    def __init__(self, func):
        super(PersistentlyMemoizedFunction, self).__init__(func)
        cache_file_name = os.path.join(persistence.persistent_cache_directory, "{0}.pickle".format(func.__name__))
        self._cache = PersistentDictionary(cache_file_name)

memoized = MemoizedFunction
persistently_memoized = PersistentlyMemoizedFunction
__all__ = ['memoized', 'persistently_memoized']