class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num==1:
            return 1
        
        l = 1
        r = num
        
        while l<=r:
            
            mid = (l+r)//2
            
            curr = mid**2
            
            if curr==num:
                return True
            elif curr>num:
                r = mid-1
            else:
                l = mid+1
        
        
        # if l**2==num:
        #     return True
        
        return False
            
        