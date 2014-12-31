import os
import os.path

CACHE_DIRECTORY_NAME = "persistent_memoization_cache"

module_directory = os.path.dirname(os.path.join(os.getcwd(), __file__))
persistent_cache_directory = os.path.join(module_directory, CACHE_DIRECTORY_NAME)

if not os.path.exists(persistent_cache_directory):
    os.mkdir(persistent_cache_directory)