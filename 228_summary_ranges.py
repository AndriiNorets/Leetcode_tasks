class Solution:
    def summaryRanges(self, nums: int) -> str:
        result = []
        nums  += [1000]
        list_to_add = []
        for item in range(len(nums)-1):
            list_to_add.append(nums[item])
            if nums[item] != nums[item+1]-1:
                if len(list_to_add) == 1:
                    result.append(str(list_to_add[0]))
                else:
                    result.append(f"{list_to_add[0]}->{list_to_add[-1]}")

                list_to_add = []

        return result