class Solution(object):
    def isPalindrome(self, x):
        return x >= 0 and str(x) == str(x)[::-1]  
        