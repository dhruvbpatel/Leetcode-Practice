

from typing import List
class Solution:
    
    #bfs algo
    def detect(self,adj,visited,curr):
        
        visited[curr]=1
        
        q=[]
        q.append([curr,-1])
        
        while q:
            curr = q.pop(0)
            node = curr[0]
            parent = curr[1]
            
            for adjnode in adj[node]:
                if visited[adjnode]==0:
                    visited[adjnode]=1
                    q.append([adjnode,node])
                elif(parent!=adjnode):
                    return True #cycle exist as we come across node which is not parent and is visited
        return False
        
    
    def dfs(self,adj,visited,curr,parent):
        
        visited[curr]=1
        
        for adjnode in adj[curr]:
            if visited[adjnode]==0:
                if self.dfs(adj,visited,adjnode,curr):
                    return True
            elif parent!=adjnode:
                return True
        
        return False
                
                
    
    
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		
		visited = [0]*V
		
		for i in range(V):
		    if visited[i]==0:
		      #  if self.detect(adj,visited,i):
		      #      return True
		      if self.dfs(adj,visited,i,-1):
		          return True
		
		return False


#{ 
 # Driver Code Starts


if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends