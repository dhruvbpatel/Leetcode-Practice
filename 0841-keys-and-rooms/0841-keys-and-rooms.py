class Solution:
    
    def mark(self,curr,adj,visited,rooms):
        
        visited[curr]=1
        
        for node in adj[curr]:
            if visited[node]==0:
                self.mark(node,adj,visited,rooms)
                
        
    
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        #make adj matrix
        # dfs
        #if all visited-> true else false
        
        n = len(rooms)
        adj = defaultdict(list)
        
        visited = [0]*len(rooms)
        
        for i in range(len(rooms)):
            adj[i].extend(list(rooms[i]))
        
        # print(adj)
        
        for curr in visited:
            if curr==0:
                self.mark(curr,adj,visited,rooms)
        
        for i in visited:
            if i==0:
                return False
        
        return True
        
        