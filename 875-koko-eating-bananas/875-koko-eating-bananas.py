class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        #min val for k can be 1 and max can be max(piles)
        # as value greater than that is of no good as result will be same
        l,r = 1,max(piles)
        ans = r  #initially take ans = r
        
        while l<=r:
            
            k = (l+r)//2  # find mipoint as our k
            hours = 0   # hours to eat all with current k
            
            for p in piles: #iterate over all piles
                hours+=math.ceil(p/k) #get hours with current k
            
            if hours<=h: #if it satisfies under h then update ans
                ans = min(ans,k)
                r = k-1 #also go to left to find minimum
            
            else: #go to right
                l = k+1
        
        return ans
            
            
            
            
        
        