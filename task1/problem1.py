class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        else:
            cur_length = 1
            max_length = 1
            for i in range(len(nums)-1):
                if nums[i] < nums[i+1]:
                    cur_length+=1
                else:
                    max_length = cur_length
                    cur_length=1
        return max_length