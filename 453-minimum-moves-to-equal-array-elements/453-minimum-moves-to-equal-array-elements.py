class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        mn = min(nums)
        
        ans = 0
        
         
        #// the ans is equivalent to no of moves required to decrement alll elements of array to min element of array
        
        for i in range(0,len(nums)):
            
            ans+=(nums[i]-mn)
        
        return ans