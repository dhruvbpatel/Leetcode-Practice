class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        ans = []
        
        for i in range(len(intervals)):
            
            # less than current
            if newInterval[1]<intervals[i][0]:
                ans.append(newInterval)
                return ans + intervals[i:]
                            
            elif newInterval[0] > intervals[i][1]:  ## if bigger than current
                ans.append(intervals[i])
            
            else:
                
                # if overlapping on either side
                
                # update min and max of newinterval
                newInterval = [min(newInterval[0],intervals[i][0]),
                               max(newInterval[1],intervals[i][1])]
            
        ans.append(newInterval) # if it is not returned in 1st case then in end we need to append
        
        return ans
            
            
            
        