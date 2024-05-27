class Solution(object):
    def romanToInt(self, s):
        result = 0
        roman_int = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1,
        }
        item = 0

        if len(s) == 1:
            return roman_int[s[0]]

        while item < len(s) - 1:
            current = roman_int[s[item]]
            next = roman_int[s[item + 1]]
            if next > current:
                result += next - current
                item += 2
                continue

            result += roman_int[s[item]]
            item += 1

        if roman_int[s[-2]] >= roman_int[s[-1]]:
            result += roman_int[s[-1]]
        return result