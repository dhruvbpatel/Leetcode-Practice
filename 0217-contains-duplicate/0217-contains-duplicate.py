class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        mp = defaultdict(int)
        
        for n in nums:
            
            if n not in mp:
                mp[n]+=1
            else:
                return True
            
        return False