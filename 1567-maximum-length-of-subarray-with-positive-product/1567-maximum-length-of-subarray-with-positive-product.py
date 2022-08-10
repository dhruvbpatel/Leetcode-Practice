class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        pos = 0
        neg = 0
        
        if len(nums)==0:
            return 0
        
        ans = 0
        
        for i in range(len(nums)):
            
            if nums[i]==0:
                pos = 0
                neg = 0
                continue
            
            
            if nums[i]>0:
                
                pos+=1
                neg = 0 if neg==0 else neg+1
            
            elif nums[i]<0:
                
                temp = pos
                pos = 0 if neg==0 else neg+1
                neg = temp+1
            
            ans = max(ans,pos)
    
        
        return ans
                
                
                
            
        