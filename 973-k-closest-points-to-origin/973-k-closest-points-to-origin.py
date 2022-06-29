class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        d =  []
        
        for curr in points:
            dist = (curr[0])**2 + (curr[1])**2
            d.append([-dist,[curr[0],curr[1]]])
        
        heapq.heapify(d)
                
        order = heapq.nlargest(k,d) 
        
        ans = []
        
        for i in order:
            ans.append(i[1])
        return ans
      
        
        
        