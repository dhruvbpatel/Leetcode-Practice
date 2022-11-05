#User function Template for python3

class Solution:
    
    def dfs(self,visited,adj,ans,curr):
        
        for node in adj[curr]:
            if visited[node]!=1:
                visited[node]=1
                ans.append(node)
                self.dfs(visited,adj,ans,node)
        
        return ans
        
        
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        visited = [0]*V
        ans = []
        visited[0]=1    
        ans.append(0)
        return self.dfs(visited,adj,ans,0)
        
        


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends