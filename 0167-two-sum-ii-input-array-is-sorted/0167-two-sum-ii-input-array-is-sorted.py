class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        
        start=0
        end=length-1
        
        while start<=end:
            if nums[start]+nums[end]==target:
                return [start+1,end+1]
            
            elif nums[start]+nums[end]<target:
                start+=1
            
            else:
                end-=1
        
        return -1
        
        
            
            
        