class Solution(object):
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)

        final = set1.intersection(set2)
        return list(final)
    
solution = Solution()
print(solution.intersection([1, 2, 2, 1], [2, 2]))