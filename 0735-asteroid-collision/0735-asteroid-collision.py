class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        st = []
        
        for curr in asteroids:
            
            #if +ve append only
            if curr>0:
                st.append(curr)
            
            else:
                #if st and only if top is +ve and abs(new -ve ) > then top , we pop 
                # else top will be top only , new will be destroeyed
                while st and st[-1]>0 and st[-1]<abs(curr):
                    st.pop()
                
                #if st empty or only -ve
                if not st or st[-1]<0:
                    st.append(curr) #append curr
                
                elif st[-1]==-curr: #curr is -ve still so if +ve - -ve then both destroyed
                    st.pop()
                
        return st
        