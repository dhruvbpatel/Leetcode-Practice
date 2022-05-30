#User function Template for python3

class Solution:
    def findPath(self, arr, n):
        
        # code here
        res = []
        vis = [[0 for i in range(n)] for j in range(n)]
        
        def solve(i, j, st=""):
            
            if i==n-1 and j==n-1:
                res.append(st)
                return
            
            # Downward
            if i+1<n and arr[i+1][j] == 1 and vis[i+1][j] == 0:
                vis[i][j] = 1
                solve(i+1, j, st+"D")
                vis[i][j] = 0
            
            # Left
            if j-1>=0 and arr[i][j-1] == 1 and vis[i][j-1] == 0:
                vis[i][j] = 1
                solve(i, j-1, st+"L")
                vis[i][j] = 0
            
            # Right
            if j+1<n and arr[i][j+1] == 1 and vis[i][j+1] == 0:
                vis[i][j] = 1
                solve(i, j+1, st+"R")
                vis[i][j] = 0
            
            # Upward
            if i-1>=0 and arr[i-1][j] == 1 and vis[i-1][j] == 0:
                vis[i][j] = 1
                solve(i-1, j, st+"U")
                vis[i][j] = 0
            
        if arr[0][0]:
            solve(0, 0)
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends