class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        nums.sort()
        ans  = 0
        for i in range(1,len(nums)):
            
            # while nums[i]<=nums[i-1]:
            #     nums[i]+=1
            #     ans+=1
            if nums[i]<=nums[i-1]:
                diff = abs(nums[i-1]-nums[i])+1
                ans+=diff
                nums[i]+=diff
                
        
        return ans