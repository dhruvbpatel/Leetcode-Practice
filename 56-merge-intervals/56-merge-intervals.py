class Solution:
    def merge(self, arr: List[List[int]]) -> List[List[int]]:
        
        arr.sort()
        
        ans = []
        
        temp = arr[0]
        
        for it in arr:
            
            if it[0]<=temp[1]:
                temp[1] = max(it[1],temp[1])
            else:
                ans.append(temp)
                temp = it
        
        ans.append(temp)
        
        return ans
    