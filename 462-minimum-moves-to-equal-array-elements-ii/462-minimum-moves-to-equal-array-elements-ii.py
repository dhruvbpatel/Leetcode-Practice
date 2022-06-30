class Solution:
    def minMoves2(self, nums: List[int]) -> int:

        nums = sorted(nums)
        
#         mn = sys.maxsize
#         sm = 0 #sum before k
#         total = sum(nums)
        
        
        
#         for i in range(len(nums)):
#             ans = (nums[i]*i - sm) + ((total-sm)-(nums[i]*(len(nums)-i)))
#             mn  = min(mn,ans)
#             sm+=nums[i]
        
#         return mn

        #approach 2: using median as point at which we eventually settle
    
        ans = 0
        
        for num in nums:
            ans+=abs(nums[len(nums)//2]-num)  #finding median as n+1/2 
        
        return ans
        
        
        
        
            
        