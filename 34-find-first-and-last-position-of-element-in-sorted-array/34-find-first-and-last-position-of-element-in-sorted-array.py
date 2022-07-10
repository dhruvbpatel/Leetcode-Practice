class Solution:
    
    def findBound(self,nums,target,findLB):
        
        l = 0
        r = len(nums)-1
        
        while l<=r:
            
            mid = (l+r)//2
            
            if nums[mid]==target:
                
                #find lowerbound
                if findLB == True:
                    
                    if mid==l or nums[mid-1]!=target:
                        return mid
                    else:
                        r = mid-1 # as lower bound search in right
                
                else:
                    # find upper bound
                    
                    if mid==r or nums[mid+1]!=target:
                        return mid
                    else:
                        l = mid+1
                        
            elif(nums[mid]<target):
                l = mid+1
            else:
                r = mid-1
        
        return -1
        
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        lower_bound = self.findBound(nums,target,True)
        
        if lower_bound == -1:
            return [-1,-1]
        
        upper_bound = self.findBound(nums,target,False)
        
        return [lower_bound,upper_bound]
        