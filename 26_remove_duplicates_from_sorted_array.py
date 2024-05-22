class Solution(object):
    def removeDuplicates(self, nums):
        idx = 0
        unique_set = set()
        for elem in nums:
            if elem not in unique_set:
                unique_set.add(elem)
                nums[idx] = elem
                idx += 1

        for item in range(len(unique_set),len(nums)):
            nums.pop()