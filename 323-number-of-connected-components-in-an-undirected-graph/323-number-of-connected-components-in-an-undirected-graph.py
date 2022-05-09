class Solution:
    
    def dfs(self,adj,visited,curr):
        visited[curr] = 1
        
        for i in adj[curr]:
            if visited[i]==0:
                self.dfs(adj,visited,i)
        
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
            
        visited =[0]*(n)
        ans = 0
        for i in range(len(visited)):
            if visited[i]==0:
                self.dfs(adj,visited,i)
                # if(visited[i]==1):
                ans+=1
        
        return ans
                
            
            
            
            
        