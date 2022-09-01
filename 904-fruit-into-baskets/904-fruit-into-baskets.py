class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        l = 0
        ans = 0
        d = dict()
        
        for r in range(len(fruits)):
            
            r_fruit = fruits[r]
            
            if r_fruit not in d.keys():
                d[r_fruit]=0
            d[r_fruit]+=1
            
            
            while len(d)>2:
                l_fruit = fruits[l]
                
                d[l_fruit]-=1
                
                if d[l_fruit]==0:
                    del d[l_fruit]
                
                l+=1
            
            ans = max(ans,r-l+1)
        
        
        return ans
                
            
        
        
        