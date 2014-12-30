import sqlite3
import os
import time
import math

dbpath = os.path.expanduser('~/Dropbox/ITC_db/best_browse_dev.sqlite3')


def getTimeDifferences(email):
    """
    [("google.com", [1, 5, 9]), (...), ...]
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
