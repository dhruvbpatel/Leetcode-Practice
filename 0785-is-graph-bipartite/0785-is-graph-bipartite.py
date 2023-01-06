class Solution:
    
    def isPossible(self,curr,graph,color):
        
        if(color[curr]==-1): color[curr] =1
        
        for it in graph[curr]:
            if(color[it]==-1):
                color[it] = 1-color[curr]
                if(self.isPossible(it,graph,color)==False):
                    return False
            elif(color[it]==color[curr]):
                return False
        return True
        
            
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        color = [-1]*len(graph)
        
        for i in range(len(graph)):
            
            if(color[i]==-1):
                if(self.isPossible(i,graph,color)==False):
                    return False
        
        return True
            