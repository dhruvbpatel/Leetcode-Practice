class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currmax = nums[0]
        max_till_now = nums[0]
        
        for i in range(1,len(nums)):
            currmax = max(nums[i],nums[i]+currmax)
            max_till_now = max(max_till_now,currmax)
        return max_till_now
        