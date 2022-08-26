class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        # intuition is we need to take count of each element.
        
        
        def solve(temp,mp):
            
            if len(temp)==len(nums): #if temp==nums then we have our permuatation
                ans.append(list(temp)) #append
                return
            
            for num in mp: #iterate in counter
                
                if mp[num]>0:# only if mp[num] has still some value
                    
                    temp.append(num) #append, as we can 
                    mp[num]-=1 #aslo decrease count
                    
                    solve(temp,mp) #recurse
                    
                    temp.pop() #backtrack
                    mp[num]+=1
            
                    
        
        
        ans = []
        solve([],Counter(nums))
        
        return ans
        
        