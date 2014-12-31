import urllib2
import json
import os.path
import persistence
from memoization import persistently_memoized

KEY_MANAGER_FILE_NAME = 'KeyManager.json'
SIMILARWEB_URL_FORMAT = "http://api.similarweb.com/Site/{domain}/v2/alsovisited?Format={format}&UserKey={key}"
SIMILARWEB_RESPONSE_TOP_KEY = u"AlsoVisited"
SIMILARWEB_RESPONSE_URL_KEY = u"Url"
SIMILARWEB_RESPONSE_SCORE_KEY = u"Score"

class KeyManager(object):
    USES_PER_KEY = 66
    
    def __init__(self, file_path):
        self.__file_path = file_path
        with open(file_path, 'r') as ifile:
            persistent_state = json.load(ifile)
        self.__keys = persistent_state['keys']
        self.__use_count = persistent_state['use_count']

    def get_key(self):
        try:
            if self.__use_count >= KeyManager.USES_PER_KEY:
                self.__keys = self.__keys[1:]
                self.__use_count = 0
            self.__use_count += 1
            return self.__keys[0]

        finally:
            persistent_state = {'keys': self.__keys, 'use_count': self.__use_count}
            with open(self.__file_path, 'w') as ofile:
                json.dump(persistent_state, ofile)

key_manager = KeyManager(os.path.join(persistence.persistent_cache_directory, KEY_MANAGER_FILE_NAME))

@persistently_memoized
def get_correlated_websites(domain):
    similarweb_url = SIMILARWEB_URL_FORMAT.format(domain=domain, format="JSON", key=key_manager.get_key())
    try:
        response = urllib2.urlopen(similarweb_url)
    except urllib2.HTTPError:
        return ()
    response_string = response.read()
    response_dict = json.loads(response_string)
    return tuple((entry[SIMILARWEB_RESPONSE_URL_KEY].decode('utf-8'), entry[SIMILARWEB_RESPONSE_SCORE_KEY])
                 for entry in response_dict[SIMILARWEB_RESPONSE_TOP_KEY])
