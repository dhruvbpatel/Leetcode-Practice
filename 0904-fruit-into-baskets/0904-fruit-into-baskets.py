class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0 #left end of window
        ans = 0
        d = dict()
        
        # iterate over array
        for r in range(len(fruits)):
            
            r_fruit = fruits[r]
            
            
            if r_fruit not in d.keys():
                d[r_fruit]=0  #add if r_fruit not in dict
            d[r_fruit]+=1 #update count as it is now included
            
            #if dict len >2 then only we need to check to reduce window as we can only use 2 basket
            while len(d)>2:
                l_fruit = fruits[l]
                
                d[l_fruit]-=1 #decrease
                
                if d[l_fruit]==0: #if zero no need for that , delete
                    del d[l_fruit]
                # also move ahead the left end of window
                l+=1
            
            ans = max(ans,r-l+1) #at each step check and update max        
        
        return ans