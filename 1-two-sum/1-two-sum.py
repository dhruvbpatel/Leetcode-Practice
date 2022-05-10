class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mp = dict()
        ans = []
        
        for i in range(len(nums)):
            
            temp = target-nums[i]
            
            if temp in mp:
                
                ans.append(i)
                ans.append(mp[temp])
                
                return ans
            
            mp[nums[i]]=i
            
        return ans
                
            
                
        