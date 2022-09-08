class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mp = defaultdict(int)
        ans = []
        for i in range(len(nums)):
            
            find = target-nums[i]
            
            if find in mp.keys():
                ans.append(i)
                ans.append(mp[find])
                return ans
            
            mp[nums[i]]=i
        
        