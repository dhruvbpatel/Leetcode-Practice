class Solution:
    
    
    def isCyclic(self,adj,visited,curr)->bool:

            if(visited[curr]==2): return True

            visited[curr]=2

            for node in adj[curr]:
                if(visited[node]!=1):
                    if(self.isCyclic(adj,visited,node)):
                        return True


            visited[curr]=1
            return False;
        
    
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = defaultdict(list) # eg: of type adj = {0:[1],1:[0]}
        
        for i in prerequisites:
            adj[i[0]].append(i[1])
        
        visited = [0]*numCourses

        for i in range(0,numCourses):
            if(visited[i]==0):
                if(self.isCyclic(adj,visited,i)):
                    return False
            
        return True
               
        
        
        