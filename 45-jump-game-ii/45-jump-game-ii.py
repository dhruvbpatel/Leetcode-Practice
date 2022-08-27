class Solution:
    def jump(self, nums: List[int]) -> int:
        
        #we take 2 pointer l and r
        # now at curr idx we find how far we can reach
        # eg: 2  3 1  1 4 
        # currently l=0 r=0 
        # at 0 idx we see we can jump max of 2 so our next window end i.e r will be at idx=2
        # and l = r+1
        # ans+=1 because we can jump to next window now
        # do this till we reach end
        
        l = 0
        r = 0
        
        ans = 0
        
        while r<len(nums)-1:
            
            farthest = 0
            
            for i in range(l,r+1):
                farthest = max(farthest,i+nums[i])
            
            l = r+1
            r = farthest
            ans+=1
        
        return ans
                
        