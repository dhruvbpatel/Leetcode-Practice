class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        mp =defaultdict(int)
        
        for i in nums:
            mp[i]+=1
        
        for k,v in mp.items():
            if v>1:
                return True
        
        return False