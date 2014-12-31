import math
import similarweb
import operator
import utils
import sys
import heapq
from parse_domain import parse_domain

"""
ToDos:
1) Filter output list, such as  the super-popular websites
2) Add explanation for why we're suggesting it
3) Make flexible number of recommendations
"""

DISCOUNT_EXPONENT = 0.9
TOP_X = 10
#FORBIDDEN_WEBSITES = ['google','facebook','youtube','yahoo','baidu','qq','twitter','wikipedia','amazon','live','linkedin','sina','ebay','blogspot','bing','wordpress','instagram','PayPal','microsoft']

class UserBrowsingHistory(object):
    def __init__(self,userID):
        self.userID = userID
        self.visitedURLsAndTimes = utils.getTimeDifferences(self.userID)  # self.getVisitedURLsAndTimes()
        # A list of URLCount objects
        # self.visitedURLCounts = self.getVisitedURLCounts()
        self.visitedURLCounts = sorted(self.getVisitedURLCounts(), key=lambda x: x.weightedCount, reverse=True)[:TOP_X]
        self.fillInRelatedPagesHash()

    # def getVisitedURLsAndTimes(self):
    #     return utils.getTimeDifferences(self.userID)

    def getParsedDomain(self, domain):
        returnthis = parse_domain(domain, 2).split('.', 1)[0]
        if returnthis == '':
            returnthis = parse_domain('http://' + domain, 2).split('.', 1)[0]
        return returnthis

    def getVisitedURLCounts(self):
        self.visitedURLDomains = set()
        for urlAndTime in self.visitedURLsAndTimes:
            # could use tld.get_tld instead of parse_domain
            self.visitedURLDomains.add(self.getParsedDomain(urlAndTime[0]))
        return [URLCount(urlAndTime[0], urlAndTime[1]) for urlAndTime in self.visitedURLsAndTimes]# if parse_domain(urlAndTime[0],2).split('.', 1)[0] not in FORBIDDEN_WEBSITES]

    def fillInRelatedPagesHash(self):
        self.recsHash = {}
        for visitedURL in self.visitedURLCounts:
            self.addRelatedURLtoHash(visitedURL)

    def addRelatedURLtoHash(self, visitedURL):
        visitedURL.setRelatedWebsites()
        for relatedWebsite in visitedURL.relatedWebsites:
            urlName = relatedWebsite[0]
            urlScore = relatedWebsite[1]
            shortURLName = self.getParsedDomain('http://' + urlName)
            if any(urlString == shortURLName for urlString in self.visitedURLDomains):
                #print "filtered1 "+urlName
                continue
##            urlRedirectName = utils.getRedirect('http://' + urlName)
##            if urlRedirectName != urlName:
##               if any(urlCount.urlString == urlRedirectName for urlCount in self.visitedURLCounts):
##                   #print "filtered2 " + urlRedirectName
##                   continue
            incrementScore = self.getIncrementScore(visitedURL.weightedCount,urlScore)
            if urlName not in self.recsHash:
                self.recsHash[urlName] = 0.0
            self.recsHash[urlName] += incrementScore

    def getIncrementScore(self,visitedWeightedCount,relatedScore):
        return visitedWeightedCount * relatedScore

    def getRecommendation(self):
        ## k = min(k,len(self.recsHash.keys()))
        nRecommends = 5
        sortedKeys = heapq.nlargest(nRecommends, self.recsHash, key=self.recsHash.get)
        return [utils.getRedirect("http://"+key) for key in sortedKeys[0:nRecommends] if utils.getRedirect("http://"+key) is not None]
        #return sortedKeys[0:5]
        #return max(self.recsHash.iteritems(), key=(lambda (key, value): value))[0]



class URLCount(object):
    def __init__(self, urlString, timeDifferences):
        self.urlString = urlString
        self.weightedCount = self.getWeightedCount(timeDifferences)
        # self.relatedWebsites = self.getRelatedWebsites()

    def getWeightedCount(self, timeDifferences):
        count = 0.0
        for timeDiff in timeDifferences:
            # adjustedTimeDiff = timeDiff  # self.getAdjustedTimeDifference(timeDiff)
            count = count + 1.0 / math.pow(float(timeDiff), DISCOUNT_EXPONENT)
        return count

    ## @staticmethod
    ## def getAdjustedTimeDifference(timeDiff):
    ##     if timeDiff < 0:
    ##         raise ValueError("Time difference should be nonnegative.")
    ##     return timeDiff + 1

    def setRelatedWebsites(self):
        #return [("google.com",.2),("mit.edu",.12),("arkiv.org",.1)]
        webCorrelations = similarweb.get_correlated_websites(self.urlString)
        self.relatedWebsites = [(str(correlation[0]), correlation[1]) for correlation in webCorrelations]

def main():
    browser_id = sys.argv[1]
    print UserBrowsingHistory(browser_id).getRecommendation()

if __name__ == '__main__':
    main()
