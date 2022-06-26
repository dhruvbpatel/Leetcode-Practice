class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # zip p and s in one array
        pair = [[p,s] for p,s in zip(position,speed)]
        
        st = []
        
        # start from reverse sorted
        for p,s in sorted(pair)[::-1]:
            st.append((target-p)/s) #append in st
            
            #if len>=2 and if cars colliding then pop latest
            if len(st)>=2 and st[-1]<=st[-2]:
                st.pop()
        
        # final ans is len of fleet in stack
        return len(st)
        
        