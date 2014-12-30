import math

class UserBrowingHistory:
    def __init__(self,userName):
        self.userName = userName
        self.visitedURLs = self.getVisitedURLs()
        self.recsHash = {}

    def getVisitedURLs(self):
        """
        returns a list of URLCount objects
"""

    def getRecommendation(self):
        for visitedURL in self.visitedURLs:
            self.addRelatedURLtoHash(visitedURL)
            

    def addRelatedURLtoHash(self,visitedURL):
        for relatedWebsite in visitedURL.relatedWebsites:
            urlName = relatedWebsite.name
            urlScore = relatedWebsite.urlInverseRank
            if urlName not in self.visitedURLs:
                incrementScore = getIncrementScore(self,visitedWeightedCount,urlScore)
                if urlName not in self.recsHash.keys():
                    self.recsHash[urlName] = 0.0
                self.recsHash[urlName] = self.recsHash[urlName] + incrementScore
        
    def getIncrementScore(self,visitedWeightedCount,relatedScore):
        return visitedWeightedCount*relatedScore
    
class URLCount:
    def __init__(self,urlString):
        self.urlString = urlString
        self.timeDifferences = self.getVisitLog(urlString)
        self.weightedCount = self.getWeightedCount()
        self.relatedWebsites = self.getRelatedWebsites(self.urlString)

    def getWeightedCount(self):
        count = 0.0
        for timeDiff in self.timeDifferences:
            adjustedTimeDiff = self.getAdjustedTimeDifference(timeDiff)
            count = count + 1.0/math.pow(float(adjustedTimeDiff),.3)
        return count

    @staticmethod
    def getAdjustedTimeDifference(timeDiff):
        if timeDiff <= 0:
            raise NameError("time Difference should be positive.")
        return timeDiff+1

    @staticmethod
    def getVisitLog(urlString):
        """ returns an array of floats [t1,...,tn], where each time
            is the time, in days, since that visit.
            For instance, [0.5,2.2] means that the user has visited
            urlString twice: half-day ago and 2.2 days ago.
            
    """
        diffs = [1,4,9]
        return diffs

    @staticmethod
    def getRelatedWebsites(urlString):
        """
        returns a list of related websites, where each item in the list
        is a pair [urlString,important], i.e. ["google.com",0.051341]
"""
    @staticmethod
    def sortRelatedWebsites(websiteCorrelations):
        
    
