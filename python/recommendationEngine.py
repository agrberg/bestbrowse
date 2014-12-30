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
4) Adjust for seconds
"""

DISCOUNT_EXPONENT = 0.9
#FORBIDDEN_WEBSITES = ['google','facebook','youtube','yahoo','baidu','qq','twitter','wikipedia','amazon','live','linkedin','sina','ebay','blogspot','bing','wordpress','instagram','PayPal','microsoft']

class UserBrowsingHistory(object):
    def __init__(self,userEmail):
        self.userEmail = userEmail
        self.visitedURLsAndTimes = self.getVisitedURLsAndTimes()
        self.visitedURLCounts = self.getVisitedURLCounts()
        self.fillInRelatedPagesHash()

    def getVisitedURLsAndTimes(self):
        return utils.getTimeDifferences(self.userEmail)

    def getVisitedURLCounts(self):
        self.visitedURLDomains = set()
        for urlAndTime in self.visitedURLsAndTimes:
            self.visitedURLDomains.add(parse_domain(urlAndTime[0],2).split('.', 1)[0])
        return [URLCount(urlAndTime[0], urlAndTime[1]) for urlAndTime in self.visitedURLsAndTimes]# if parse_domain(urlAndTime[0],2).split('.', 1)[0] not in FORBIDDEN_WEBSITES]

    def fillInRelatedPagesHash(self):
        self.recsHash = {}
        for visitedURLCount in self.visitedURLCounts[:10]:
            self.addRelatedURLtoHash(visitedURLCount)

    def addRelatedURLtoHash(self, visitedURL):
        for relatedWebsite in visitedURL.relatedWebsites:
            urlName = relatedWebsite[0]
            urlScore = relatedWebsite[1]
            if any(urlCount.urlString == urlName for urlCount in self.visitedURLCounts):
                #print "filtered1 "+urlName
                continue
##            urlRedirectName = utils.getRedirect('http://' + urlName)
##            if urlRedirectName != urlName:
##               if any(urlCount.urlString == urlRedirectName for urlCount in self.visitedURLCounts):
##                   #print "filtered2 " + urlRedirectName
##                   continue

            #if parse_domain(urlName,2).split('.', 1)[0] in self.visitedURLDomains:
                #print "filtered2 "+urlName
                #continue
            #print "added "+urlName
            incrementScore = self.getIncrementScore(visitedURL.weightedCount,urlScore)
            if urlName not in self.recsHash:
                self.recsHash[urlName] = 0.0
            self.recsHash[urlName] = self.recsHash[urlName] + incrementScore

    def getIncrementScore(self,visitedWeightedCount,relatedScore):
        return visitedWeightedCount * relatedScore

    def getRecommendation(self,k=1):
        k = min(k,len(self.recsHash.keys()))
        sortedKeys = heapq.nlargest(5, self.recsHash, key=self.recsHash.get)
        return sortedKeys[0:5]
        #return max(self.recsHash.iteritems(), key=(lambda (key, value): value))[0]



class URLCount(object):
    def __init__(self, urlString, timeDifferences):
        self.urlString = urlString
        self.weightedCount = self.getWeightedCount(timeDifferences)
        self.relatedWebsites = self.getRelatedWebsites()

    def getWeightedCount(self, timeDifferences):
        count = 0.0
        for timeDiff in timeDifferences:
            adjustedTimeDiff = self.getAdjustedTimeDifference(timeDiff)
            count = count + 1.0 / math.pow(float(adjustedTimeDiff), DISCOUNT_EXPONENT)
        return count

    @staticmethod
    def getAdjustedTimeDifference(timeDiff):
        if timeDiff < 0:
            raise ValueError("Time difference should be nonnegative.")
        return timeDiff + 1

    def getRelatedWebsites(self):
        #return [("google.com",.2),("mit.edu",.12),("arkiv.org",.1)]
        webCorrelations = similarweb.get_correlated_websites(self.urlString)
        return [(str(correlation[0]), correlation[1]) for correlation in webCorrelations]

def main():
    browser_id = sys.argv[1]
    print UserBrowsingHistory(browser_id).getRecommendation()

if __name__ == '__main__':
    main()
