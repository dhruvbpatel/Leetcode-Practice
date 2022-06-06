class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(arr)-1
        ans = []
        while l<r:
            if arr[l]+arr[r]==target:
                ans.append(l+1)
                ans.append(r+1)
                return ans
            elif arr[l]+arr[r]<target:
                l+=1
            else:
                r-=1
        
        return ans
            
                
                
                
                
            
        