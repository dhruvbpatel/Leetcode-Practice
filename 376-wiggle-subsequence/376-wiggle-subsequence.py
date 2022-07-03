class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        if nums is None:
            return 0
        
        length = 1
        
        up = None
        
        for i in range(1,len(nums)):
            
            if nums[i]>nums[i-1] and up!=True:
                length+=1
                up = True
            
            if nums[i]<nums[i-1] and up!=False:
                length+=1
                up = False
        
        return length