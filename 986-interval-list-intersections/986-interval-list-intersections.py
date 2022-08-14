class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        
        #logic:
        # take 2 pointers
        # as each interval is disjoint so they'll not overlap even in same list
        # find max low and min high i.e our intersection
        #only if both intervals are intersecting, then append
        # now move ahead the lower pointer
        
        ans = []
        
        i = 0
        j = 0
        
        while i<len(A) and j<len(B):
            
            #get interval
            lo = max(A[i][0],B[j][0])
            hi = min(A[i][1],B[j][1])
            
            if lo<=hi: #only if both intervals are intersecting, then append
                ans.append([lo,hi])
            
            
            # Remove the interval with the smallest endpoint
            if A[i][1]<B[j][1]:
                i+=1
            else:
                j+=1
        
        
        return ans
        
        