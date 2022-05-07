class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        ans =[]
        temp = intervals[0]
        
        for i in intervals:
            if i[0]<=temp[1]:
                temp[1] = max(temp[1],i[1])
            else:
                ans.append(temp)
                temp = i
        
        ans.append(temp)
        return ans
        