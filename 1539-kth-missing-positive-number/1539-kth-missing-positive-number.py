class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        l = 0
        r = len(arr)-1
        
        while l<=r:
            
            mid = (l+r)//2
            
            if arr[mid]-mid-1<k: ##if missing elemenets before mid is <k then go right
                l = mid+1
            else:
                r = mid-1
        
        #here now l>r i.e l = r+1
        # and ans is between l and r
         # The number of integers missing before arr[right] is
        # arr[right] - right - 1 -->
        # the number to return is
        # arr[right] + k - (arr[right] - right - 1) = k + left
        
        return l+k
        