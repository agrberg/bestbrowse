import urllib2
import json
from memoization import persistently_memoized

SIMILARWEB_USER_KEY = "a57e330331bad92cf4745e3c0dc234c2"
SIMILARWEB_URL_FORMAT = "http://api.similarweb.com/Site/{domain}/v2/alsovisited?Format={format}&UserKey={key}"
SIMILARWEB_RESPONSE_TOP_KEY = u"AlsoVisited"
SIMILARWEB_RESPONSE_URL_KEY = u"Url"
SIMILARWEB_RESPONSE_SCORE_KEY = u"Score"

class WebsiteCorrelation(object):
    def __init__(self, url, score):
        self.url = url
        self.score = score
    def __repr__(self):
        return "{0}({1!r}, {2!r})".format(type(self).__name__, self.url, self.score) 

@persistently_memoized
def get_correlated_websites(domain):
    similarweb_url = SIMILARWEB_URL_FORMAT.format(domain=domain, format="JSON", key=SIMILARWEB_USER_KEY)
    try:
        response = urllib2.urlopen(similarweb_url)
    except urllib2.HTTPError:
        return ()
    response_string = response.read()
    response_dict = json.loads(response_string)
    return tuple(WebsiteCorrelation(entry[SIMILARWEB_RESPONSE_URL_KEY].decode('utf-8'), entry[SIMILARWEB_RESPONSE_SCORE_KEY])
                 for entry in response_dict[SIMILARWEB_RESPONSE_TOP_KEY])
