class Solution:
    def search(self, arr: List[int], target: int) -> int:
        
        if len(arr)==1:
            if arr[0]==target:
                return 0
            else:
                return -1
        
        l = 0
        r = len(arr)-1
        
        
        while l<=r:
            
            mid = (l+r)//2
            # print(mid)
            
            if arr[mid]==target:
                return mid
            
            if arr[l]<=arr[mid]:
                # left part sorted
                if target > arr[mid] or target<arr[l]:
                    l = mid+1
                else:
                    r = mid-1
            
            else:
                # right sorted
                
                if target < arr[mid] or target > arr[r]:
                    r = mid-1
                else:
                    l = mid+1
            
            
        
        return -1
        