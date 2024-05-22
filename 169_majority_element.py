class Solution(object):
    def majorityElement(self, nums):
        relations = {}
        for item in set(nums):
            input_value = {nums.count(item):item}
            relations.update(input_value)

        max_value = max(relations.keys())
        return relations[max_value]
        