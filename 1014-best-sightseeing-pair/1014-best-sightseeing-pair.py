class Solution:
    def maxScoreSightseeingPair(self, nums: List[int]) -> int:
        
# The goal is to keep track of:
# Maximum So far and add it to the cur_cell and maintain maximum result
# Here, max_so_far contains : A[i] + i
# Original Given Formula : A[i] + A[j] + i - j

# Break in two parts : A[i] + i and A[j] -j
# Keep MAX_VALUE of first part among the elements seen so far
# Add the current element to max_so_far and check the result is changing or not
# Also, keep updating the max_so_far at each step
        
        max_so_far = nums[0]
        ans = 0
        
        for i in range(1,len(nums)):
            
            ans = max(ans,max_so_far+nums[i]-i)
            max_so_far = max(max_so_far,nums[i]+i)
        
        return ans