class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # if doubt read official solution 2
        
        if len(nums)==0:
            return 0
        
        max_till_now = nums[0]
        min_till_now = nums[0]
        ans = max_till_now
        
        for i in range(1,len(nums)):
            
            curr = nums[i]
            
            temp_max = max(curr,curr*max_till_now,curr*min_till_now)
            min_till_now = min(curr,curr*max_till_now,curr*min_till_now)
            
            max_till_now = temp_max #update max_till_now only after min operation is complete
            
            ans = max(max_till_now,ans)
        
        return ans
        
        