class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        #for it to be a valid tree, we need to have n-1 edges otherwise it will be cycle
        # and it should not be disconnected, for this we do bfs and mark all visited
        # if any is left then len(visit)!=n thus disconnected and not tree
        
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
        
        
        
        