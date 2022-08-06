class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr_sum = 0
        max_sum = -1*sys.maxsize-1
        
        for num in nums:
            curr_sum+=num
            
            
            max_sum = max(max_sum,curr_sum)
            curr_sum = max(curr_sum,0)
            
        return max_sum
            
        
        max_till_now = nums[0]
        curr_max = nums[0]
        
        for i in range(1,len(nums)):
            
            curr_max = max(curr_max+nums[i],nums[i])
            max_till_now = max(max_till_now,curr_max)
    
        return max_till_now
        