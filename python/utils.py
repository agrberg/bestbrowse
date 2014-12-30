import sqlite3
import os

dbpath = os.path.expanduser('~/Dropbox/ITC_db/best_browse_dev.sqlite3')


def getTimeDifferences(email):
    """
    [("google.com", [1, 5, 9]), (...), ...]
    """
    db = sqlite3.Connection(dbpath)
    url_times = [(str(url), int(time)) for url, time in db.execute("SELECT url, strftime('%s', visit_at) FROM visits")]
    time_dict = {}
    for url, _ in url_times:
        if url is not None:
            time_dict[url] = (url, [])
    for url, time in url_times:
        if url is not None:
            time_dict[url][1].append(time)
    return time_dict.values()


# For testing
if __name__ == '__main__':
    getTimeDifferences('dummyarg')
