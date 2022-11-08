class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        l = 0
        r = len(nums)-1
        
        ans = -1
        # print(nums)
        
        if nums[0]>k:
            return -1
        
        while l<r:
            
            sm = nums[l]+nums[r]
            
            if sm<k:
                ans = max(ans,sm)
                l+=1
            else:
                r-=1
        
        return ans
        
            
        return ans