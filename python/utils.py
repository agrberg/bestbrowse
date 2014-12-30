import sqlite3
import os
import time
import math
import urllib2
import tld

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


def getRedirect(url):
    req = urllib2.Request(url)
    res = urllib2.urlopen(req)
    redirect_url = res.geturl()
    return tld.get_tld(redirect_url)


# For testing
if __name__ == '__main__':
    print getTimeDifferences()
    print
    print getTimeDifferences('101465226514644436265')
    print
    print getRedirect('http://gmail.com')
