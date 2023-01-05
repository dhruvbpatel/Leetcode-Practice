class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        if not points:
            return 0
        
        
        points.sort(key = lambda x:x[1])
        
        arrows = 1
        
        curr_end = points[0][1]
        
        for s,e in points:
            
            # if the current balloon starts after the end of another one,
            # one needs one more arrow
            
            if curr_end < s:
                arrows+=1
                curr_end = e
        
        return arrows
        