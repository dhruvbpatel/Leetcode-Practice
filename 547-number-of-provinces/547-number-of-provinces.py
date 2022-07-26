from collections import deque
class Solution:
    def dfs(self,isConnected,visited,curr):
        for j in range(len(isConnected)):
            if(isConnected[curr][j]==1 and visited[j]==0):
                visited[j]=1
                self.dfs(isConnected,visited,j)
            
            
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [0]*len(isConnected)
        ans = 0
        for i in range(len(isConnected)):
            if visited[i]==0:
                self.dfs(isConnected,visited,i)
                ans+=1
        
        return ans
        
                

                
                
            
                
        