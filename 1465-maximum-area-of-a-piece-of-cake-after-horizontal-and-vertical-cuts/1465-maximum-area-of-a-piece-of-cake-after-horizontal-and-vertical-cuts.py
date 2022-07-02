class Solution:
    
    def getMaxConsecutiveDiff(self,arr):
        ans = 0
        for i in range(0,len(arr)-1):
            ans = max(ans,arr[i+1]-arr[i])
        return ans
        
        
    
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        
        hc = sorted(horizontalCuts)
        vc = sorted(verticalCuts)
        
        hc.insert(0,0)
        hc.append(h)
        
        vc.insert(0,0)
        vc.append(w)
        
        hc_max_diff = self.getMaxConsecutiveDiff(hc)
        vc_max_diff = self.getMaxConsecutiveDiff(vc)
        
        ans = (hc_max_diff * vc_max_diff)%(1000000007)
        
        return ans
        
        