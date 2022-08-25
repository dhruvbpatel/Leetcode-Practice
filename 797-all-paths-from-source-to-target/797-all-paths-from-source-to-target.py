class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        target = len(graph)-1
        ans = []
        
        def dfs(curr,temp):
            
            if curr==target:
                ans.append(list(temp))
                return
            
            for node in graph[curr]:
                temp.append(node)
                dfs(node,temp)
                temp.pop()
        
        
        temp = [0]
        dfs(0,temp)
        
        return ans