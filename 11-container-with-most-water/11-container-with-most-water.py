class Solution:
    def maxArea(self, arr: List[int]) -> int:
        
        l = 0
        r = len(arr)-1
        
        ans =0
        
        while(l<r):
            
            ans = max(ans,min(arr[l],arr[r])*(r-l))
            
            if(arr[l]<arr[r]):
                l+=1
            else:
                r-=1
        
        
        return ans
        