from collections import defaultdict


def isCyclic(adj,visited,curr)->bool:
        
        if(visited[curr]==2): return True
    
        visited[curr]=2
        
        for i in range(len(adj[curr])):
            if(visited[adj[curr][i]]!=1):
                if(isCyclic(adj,visited,adj[curr][i])):
                    return True
                
            
        visited[curr]=1
        return False;
    

class Solution:
    
    
        
    
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = defaultdict(list) # eg: of type adj = {0:[1],1:[0]}
        
        for i in prerequisites:
            adj[i[0]].append(i[1])
        
        visited = [0]*numCourses

        for i in range(0,numCourses):
            if(visited[i]==0):
                if(isCyclic(adj,visited,i)):
                    return False
            
        return True
               
        
        
        