class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans = 0
        minleft = prices[0]
        for i in prices:
            
            minleft = min(i,minleft)
            ans=max(ans,i-minleft)
            
        return ans
            
        