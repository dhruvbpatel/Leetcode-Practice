class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        if n==0:
            return 0
        
        k = n-2
        l = n-1
        
        while k>=0:
            
            if nums[k]<nums[k+1]:
                break
            k-=1
        
        if k<0:
            
            nums[:] = nums[::-1]
            
            
        else:
            
            while l>k:
                
                if nums[l]>nums[k]:
                    break
                
                l-=1
            
            nums[l],nums[k] = nums[k],nums[l]
            
            nums[k+1:] = nums[k+1:][::-1]
        