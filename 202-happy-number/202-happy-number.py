class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sumOfSquares(n):
            ans = 0
            
            while n:
                n,digit = divmod(n,10)
                ans+=digit**2
            return ans
        
        
        visited = set()
        
        while n not in visited:
            
            visited.add(n)
            n = sumOfSquares(n)
            
            if n==1:
                return True
            
        return False
        