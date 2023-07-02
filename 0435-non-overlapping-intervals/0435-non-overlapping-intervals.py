class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        
        ans = 0
        
        prevEnd = intervals[0][1]
        
        for start,end in intervals[1:]:
            
            if start>=prevEnd:
                prevEnd = end
            else:
                #overlapping, remove one with max end val and keep with minend
                
                ans+=1
                prevEnd = min(end,prevEnd) ##keep min end
            
        return ans
                
        