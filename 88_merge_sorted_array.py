class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for idx in range(m):
            optional = nums1[idx]
            nums2 = sorted(nums2)
            for idx_2 in range(n):
                if nums2[idx_2] < optional:
                    time_variable = optional
                    optional = nums2[idx_2]
                    nums2[idx_2] = time_variable
                    break

            nums1[idx] = optional

        nums2 = sorted(nums2)
        for item in range(m,m+n):
            nums1[item] = nums2[item - m]


        