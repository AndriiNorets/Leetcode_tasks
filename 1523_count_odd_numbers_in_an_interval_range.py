class Solution(object):
    def countOdds(self, low, high):
        if high %2 !=0 or low %2 !=0:
            return int((high - low) /2) +1
        return int((high - low) /2)
        