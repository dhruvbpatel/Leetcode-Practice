class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        if nums is None:
            return 0
        
        length = 1
        
        up = None #initially it can be anything increasing or decreasing
        
        for i in range(1,len(nums)):
            
            if nums[i]>nums[i-1] and up!=True:  # increasing seq and up is False then wiggle is there, add 
                length+=1
                up = True
            
            elif nums[i]<nums[i-1] and up!=False: #if decreasing seq and up is True then wiggle is there , add
                length+=1
                up = False
        
        return length 