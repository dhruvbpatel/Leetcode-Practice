class Solution:
    
    def dfs(self,curr,graph,color):
        
        if(color[curr]==-1): color[curr] =1
        
        for it in graph[curr]:
            if(color[it]==-1):
                color[it] = 1-color[curr]
                if(not self.dfs(it,graph,color)):
                    return False
            elif(color[it]==color[curr]):
                return False
        return True
        
        
        
    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        color = [-1]*len(graph)
        
        for i in range(len(graph)):
            
            if(color[i]==-1):
                if(not self.dfs(i,graph,color)):
                    return False
        
        return True
            