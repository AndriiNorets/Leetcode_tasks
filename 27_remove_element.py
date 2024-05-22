class Solution(object):
    def removeElement(self, nums, val):
        remowe_times = nums.count(val)
        while remowe_times >0:
            nums.remove(val)
            nums.append('_')
            remowe_times -=1
        
        return len(nums) - nums.count('_')
        