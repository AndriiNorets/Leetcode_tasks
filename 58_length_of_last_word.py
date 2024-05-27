class Solution(object):
    def lengthOfLastWord(self, s):
        result = 0
        item = -1
        s = s.rstrip()
        if ' ' not in s:
            return len(s)
        while s[item] != ' ':
            result += 1
            item -= 1

        return result