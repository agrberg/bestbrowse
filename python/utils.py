import sqlite3
import os
import time
import math

dbpath = os.path.expanduser('~/Dropbox/ITC_db/best_browse_dev.sqlite3')


def getTimeDifferences(email):
    """
    Returns a list of tuples. Each tuple is of the form (url, time_list), where
    time_list is a list of integers. For each integer i in the list, we know
    that the url was accessed i seconds ago.
    For example: [('google.com', [1, 4, 6]), ('bing.com', [100])]
    """
    curtime = int(math.ceil(time.time()))
    db = sqlite3.Connection(dbpath)
    url_times = [(str(url), int(access_time)) for url, access_time in db.execute("SELECT url, strftime('%s', visit_at) FROM visits") if url is not None]
    time_dict = {}
    for url, _ in url_times:
        time_dict[url] = (url, [])
    for url, access_time in url_times:
        time_dict[url][1].append(curtime - access_time)
    return time_dict.values()


# For testing
if __name__ == '__main__':
    print getTimeDifferences('dummyarg')
