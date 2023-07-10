class Solution:
    
    def dfs(self,adj,visited,curr):
        
        for node in adj[curr]:
            if visited[node]==0:
                visited[node]=1
                self.dfs(adj,visited,node)
        return         
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visited=[0]*n
        
        ans = 0
        
        adj = defaultdict(list)
        
        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        
        for i in range(n):
            if visited[i]==0:
                visited[i]=1
                self.dfs(adj,visited,i)
                ans+=1
        
        return ans