class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return nums[0]
        
        l = 0
        r = len(nums)-1
        
        
        if nums[l]<nums[r]: # no rotation
            return nums[l]
        
        while l<=r:
            
            mid = l + (r-l)//2  #find mid
            
            if nums[mid]>nums[mid+1]: #mid+1 is smallest so point of change
                return nums[mid+1]
            
            if nums[mid-1]>nums[mid]: # if mid-1>mid then mid is ans
                return nums[mid]
            
            if nums[mid]>nums[0]: #if mid is > idx=0 then ans is in right
                l = mid+1
            else:
                r = mid-1 ## else ans is in left
                
            
        
        
        