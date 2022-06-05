class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        mp = {}
        
        for i in range(len(nums)):
            curr = target-nums[i]
            
            if curr in mp:
                ans.append(i)
                ans.append(mp[curr])
                return ans
            
            else:
                
                mp[nums[i]]=i
    
        return ans