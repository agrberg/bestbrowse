import urllib2
import json
from memoization import persistently_memoized

SIMILARWEB_USER_KEY = "53a9eee98ccd6047db1ba4c1c9847943"
SIMILARWEB_URL_FORMAT = "http://api.similarweb.com/Site/{domain}/v2/alsovisited?Format={format}&UserKey={key}"
SIMILARWEB_RESPONSE_TOP_KEY = u"AlsoVisited"
SIMILARWEB_RESPONSE_URL_KEY = u"Url"
SIMILARWEB_RESPONSE_SCORE_KEY = u"Score"

@persistently_memoized
def get_correlated_websites(domain):
    similarweb_url = SIMILARWEB_URL_FORMAT.format(domain=domain, format="JSON", key=SIMILARWEB_USER_KEY)
    try:
        response = urllib2.urlopen(similarweb_url)
    except urllib2.HTTPError:
        return ()
    response_string = response.read()
    response_dict = json.loads(response_string)
    return tuple((entry[SIMILARWEB_RESPONSE_URL_KEY].decode('utf-8'), entry[SIMILARWEB_RESPONSE_SCORE_KEY])
                 for entry in response_dict[SIMILARWEB_RESPONSE_TOP_KEY])
