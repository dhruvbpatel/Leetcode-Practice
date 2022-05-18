class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        def dfs(curr,dest,seen):
            
            if curr==dest:
                return True
            
            if curr in seen:
                return False
            
            seen.add(curr)
            
            for i in adj[curr]:
                if dfs(i,dest,seen):
                    return True
            
            return False
            
        
        adj = defaultdict(list)
        
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        seen =set()
        
        return dfs(source,destination,seen)
        