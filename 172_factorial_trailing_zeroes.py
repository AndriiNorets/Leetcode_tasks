import math

class Solution(object):
    def trailingZeroes(self, n):
        factorial_n = math.factorial(n)
        idx = -1
        array = str(factorial_n)
        result = 0
        while array[idx] == '0' and -idx < len(array) :
            result+=1
            idx-=1

        return result