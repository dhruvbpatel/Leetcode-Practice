class Solution:
    
    def dfs(self,curr,graph,temp,target,ans):
        
        if curr==target:
            ans.append(list(temp))
            return
        
        for node in graph[curr]:
            temp.append(node)
            self.dfs(node,graph,temp,target,ans)
            temp.pop()
        
        
            
            
    
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        
        temp = [0]
        target = len(graph)-1
        ans = []
        self.dfs(0,graph,temp,target,ans)
        
#         target = len(graph)-1
#         ans = []
        
#         def dfs(curr,temp):
            
#             if curr==target:
#                 ans.append(list(temp))
#                 return
            
#             for node in graph[curr]:
#                 temp.append(node)
#                 dfs(node,temp)
#                 temp.pop()
        
        
#         temp = [0]
#         dfs(0,temp)
        
        return ans