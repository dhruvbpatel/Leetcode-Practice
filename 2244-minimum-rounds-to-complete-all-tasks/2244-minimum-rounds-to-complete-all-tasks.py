class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        
        mp = Counter(tasks)
        
        ans = 0
        
        for val in mp.values():
            
            if val==1:
                return -1
            
            ans += (val+2)//3  #this handles all cases of 2 and 3 combinations
        
        return ans
        