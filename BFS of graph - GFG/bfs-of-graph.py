#User function Template for python3

class Solution:
    
    
        
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # code here
        
        visited = [0]*V
        q = []
        q.append(0)
        visited[0]=1
        
        ans = []
        
        while q:
            
            curr = q.pop(0)
            
            ans.append(curr)
            
            for node in adj[curr]:
                if visited[node]!=1:
                    visited[node]=1
                    q.append(node)
            
                
        
        return ans
        


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
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends