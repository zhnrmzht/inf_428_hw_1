class Solution(object):
    def findLengthOfLCIS(self, nums):
        if not nums:
            return 0
        
        cur_length = 1
        max_length = 1

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                cur_length+=1
            else:
                max_length = max(max_length, cur_length)
                cur_length=1
        return max(max_length, cur_length)
    
solution = Solution()
print(solution.findLengthOfLCIS([1, 3, 5, 4, 7, 8, 9]))