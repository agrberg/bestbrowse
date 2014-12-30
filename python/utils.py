import sqlite3
import os
import time
import math
import urllib2
import tld
import requests
from memoization import persistently_memoized

dbpath = os.path.expanduser('~/Dropbox/ITC_db/best_browse_dev.sqlite3')


def getTimeDifferences(browser_id=None):
    """
    Returns a list of tuples. Each tuple is of the form (url, time_list), where
    time_list is a list of integers. For each integer i in the list, we know
    that the url was accessed i seconds ago.
    For returned list: [('google.com', [1, 4, 6]), ('bing.com', [100])]
    If a string is provided for the |browser_id| argument, then this function
    only considers visits from the user indicated by |browser_id|.
    """
    curtime = int(math.ceil(time.time()))
    db = sqlite3.Connection(dbpath)
    sql_cmd = "SELECT base_url, strftime('%s', visit_at) FROM visits"
    if browser_id is None:
        sql_params = ()
    else:
        sql_cmd += ' WHERE browser_id = ?'
        sql_params = (browser_id,)
    url_times = [(str(url), int(access_time)) for url, access_time in db.execute(sql_cmd, sql_params) if url is not None]
    time_dict = {}
    for url, _ in url_times:
        time_dict[url] = (url, [])
    for url, access_time in url_times:
        time_dict[url][1].append(curtime - access_time)
    return time_dict.values()

@persistently_memoized
def getRedirect(url):
    """
    If |url| is a 404, returns None.
    Else, returns the top-level domain of whatever |url| redirects to.
    """
    req = urllib2.Request(url)
    try:
        res = urllib2.urlopen(req)
    except urllib2.URLError, e:
        if e.code == 404:
            return None  # indicates 404
    redirect_url = res.geturl()
    return tld.get_tld(redirect_url)


# For testing
if __name__ == '__main__':
    print getRedirect('http://gmail.com')
    print getRedirect('http://lukecarbis.github.io')
