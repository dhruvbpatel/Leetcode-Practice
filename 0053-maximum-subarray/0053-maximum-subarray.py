class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        
        curr_max = nums[0]
        max_till_now = nums[0]
        
        for i in range(1,len(nums)):
            
            curr_max = max(nums[i],curr_max+nums[i])
            max_till_now = max(max_till_now,curr_max)
        
        return max_till_now
        
        
        