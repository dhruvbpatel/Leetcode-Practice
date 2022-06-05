class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # using left , right array
#         n = len(nums)
        
#         l = [1]*n
#         r = [1]*n
        
#         for i in range(1,n):
#             l[i] = l[i-1]*nums[i-1]
        
#         for i in range(n-2,-1,-1):
#             r[i] = r[i+1]*nums[i+1]
            
        
#         ans =[1]*n
        
#         for i in range(n):
#             ans[i] = l[i]*r[i]
        
#         return ans

        
        #using only ans array 
        
        # fill left product in ans
        
        n = len(nums)
        
        ans = [1]*n
        
        # fill left arr in ans
        for i in range(1,n):
            ans[i] = ans[i-1]*nums[i-1]
        
        r = 1 # r to store right pointer
        
        # on the go update r and ans[i]
        for i in range(n-1,-1,-1):
            ans[i] = ans[i]*r
            r=r*nums[i]
        
        return ans
            
        
            
            
        
        