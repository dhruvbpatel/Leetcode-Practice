class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, r: int, c: int, dp={}) -> int:
        
        
        
        # recursion
        
#         def solve(i, j, maxMove):
#             if maxMove < 0:
#                 return 0
#             if i < 0 or i >= m or j < 0 or j >= n:
#                 return 1
            
#             a = solve(i-1, j, maxMove - 1)
#             b = solve(i+1, j, maxMove - 1)
#             c = solve(i, j-1, maxMove - 1)
#             d = solve(i, j+1, maxMove - 1)
            
#             return a + b + c + d
        
#         return solve(r, c, maxMove) % 1000000007

        #memoization
        
        if maxMove<0: return 0
        
        if not(0<=r<m and 0<=c<n): #if any out of bound
            return 1
        
        
        if (m,n,maxMove,r,c) not in dp:
            
            dp[(m,n,maxMove,r,c)] = (
                
                self.findPaths(m,n,maxMove-1,r-1,c)+
                self.findPaths(m,n,maxMove-1,r,c-1)+
                self.findPaths(m,n,maxMove-1,r+1,c)+
                self.findPaths(m,n,maxMove-1,r,c+1)
                
            )% 1000000007
        
        return dp[(m,n,maxMove,r,c)]
        
    
        
    
    