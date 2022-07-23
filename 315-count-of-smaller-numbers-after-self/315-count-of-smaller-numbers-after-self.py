from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        
        
        s = SortedList() # sorted list
        output = []
        
        
        
        for n in nums[::-1]:
            
            #bisect left find position index where n can be inserted in sorted position 
            ans = SortedList.bisect_left(s,n) 
            output.append(ans) #append idx in output
            s.add(n) #also add n in sorted list
            
#             print(s)
#             print(ans)
        
        return output[::-1] # ans is in reverse manner so reverse it
    
    
"""
ex: n=6 #started from ending
at this stage s =[1]
with bisect we find idx as 1,
there append it in output

same way for other numbers, reverse output at end

"""
    
    # TC: nlogn for sorted list
    # sorted list insertion time is logn
    
            
        