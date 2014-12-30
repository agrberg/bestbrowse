import math
import similarweb
import operator
import utils
import sys

"""
ToDos:
1) Filter output list, such as  the super-popular websites
2) Add explanation for why we're suggesting it
3) Make flexible number of recommendations
"""

DISCOUNT_EXPONENT = 0.3

class UserBrowingHistory(object):
    def __init__(self,userEmail):
        self.userEmail = userEmail
        self.visitedURLsAndTimes = self.getVisitedURLsAndTimes()
        self.visitedURLCounts = self.getVisitedURLCounts()
        self.fillInRelatedPagesHash()

    def getVisitedURLsAndTimes(self):
        """
        returns a list of URLCount objects
        Real function to be given by Aaron F.
        """
        return utils.getTimeDifferences()        

    def getVisitedURLCounts(self):
        return [URLCount(urlAndTime[0], urlAndTime[1]) for urlAndTime in self.visitedURLsAndTimes]

    def fillInRelatedPagesHash(self):
        self.recsHash = {}
        for visitedURLCount in self.visitedURLCounts:
            self.addRelatedURLtoHash(visitedURLCount)

    def addRelatedURLtoHash(self, visitedURL):
        for relatedWebsite in visitedURL.relatedWebsites:
            urlName = relatedWebsite[0]
            urlScore = relatedWebsite[1]
            if any(urlCount.urlString == urlName for urlCount in self.visitedURLCounts):
                continue
            incrementScore = self.getIncrementScore(visitedURL.weightedCount,urlScore)
            if urlName not in self.recsHash:
                self.recsHash[urlName] = 0.0
            self.recsHash[urlName] = self.recsHash[urlName] + incrementScore
        
    def getIncrementScore(self,visitedWeightedCount,relatedScore):
        return visitedWeightedCount * relatedScore

    def getRecommendation(self):
        return max(self.recsHash.iteritems(), key=(lambda (key, value): value))[0]



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
        webCorrelations = similarweb.get_correlated_websites(self.urlString)
        return [(str(correlation.url), correlation.score) for correlation in webCorrelations]


def main():
    browser_id = sys.argv[1]
    print UserBrowingHistory(browser_id).getRecommendation()

if __name__ == '__main__':
    main()
