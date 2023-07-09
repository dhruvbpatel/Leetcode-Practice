class Solution:
    
    def dfs(self,visited,isConnected,curr):
        
        visited[curr]=1
        
        for j in range(len(isConnected)):
            
            if isConnected[curr][j]==1 and visited[j]==0:
                self.dfs(visited,isConnected,j)
        
        
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited=[0]*n
        ans=0
        
        for i in range(n):
            if visited[i]==0:
                self.dfs(visited,isConnected,i)
                ans+=1
        
        return ans
        