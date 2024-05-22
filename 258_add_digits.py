class Solution(object):
    def addDigits(self, num):
        def convert(val):
            return sum(int(i) for i in str(val))

        while len(str(num)) != 1:
            num = convert(num)

        return num
        