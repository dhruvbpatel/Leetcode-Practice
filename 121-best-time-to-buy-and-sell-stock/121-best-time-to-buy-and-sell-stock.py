class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        leftmin = prices[0]
        
        for i in range(1,len(prices)):
            
            if prices[i]<leftmin:
                leftmin = prices[i]
            else:
                ans=max(ans,prices[i]-leftmin)
        
        return ans
            
            
            
        