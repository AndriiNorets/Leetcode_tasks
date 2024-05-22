class Solution(object):
    def plusOne(self, digits):
        additional_value = 1
        idx = len(digits) - 1
        while idx >= 0:
            digits[idx] += additional_value
            if digits[idx] >= 10:
                digits[idx] = 0
                idx -= 1
            else:
                additional_value = 0
                idx -= 1

        if additional_value > 0:
            return [1] + digits

        return digits
        