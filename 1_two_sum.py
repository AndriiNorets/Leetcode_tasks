class Solution(object):
    def twoSum(self, nums, target):
        for item in range(len(nums)):
            value = target-nums[item]
            if value in nums[(item+1):]:
                try:
                    return [item,nums.index(value,item+1)]
                except ValueError:
                    continue

        return []