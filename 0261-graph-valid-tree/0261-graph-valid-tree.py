class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges)!=n-1:
            return False
        
        adj = defaultdict(list)
        
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        
        visited = {0}
        q = [0]
        
        while q:
            
            curr = q.pop(0)
            
            for neighbor in adj[curr]:
                if neighbor in visited:
                    continue
                
                visited.add(neighbor)
                q.append(neighbor)
        
        return len(visited)==n
        
        
        
        