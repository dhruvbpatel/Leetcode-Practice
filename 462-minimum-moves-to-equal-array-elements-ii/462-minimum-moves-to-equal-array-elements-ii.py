class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        
        mn = sys.maxsize
        sm = 0 #sum before k
        total = sum(nums)
        
        for i in range(len(nums)):
            ans = (nums[i]*i - sm) + ((total-sm)-(nums[i]*(len(nums)-i)))
            mn  = min(mn,ans)
            sm+=nums[i]
        
        return mn
        
        
        
        
            
        