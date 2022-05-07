from collections import defaultdict

class Solution:
    
    
    def dfs(self,curr):
        
        if(self.visited[curr]==2): # mark processing
            return False # cycle detected
        
        if(self.visited[curr]==1):
            return True  # already processed, and added to ans
        
        self.visited[curr]=2 # mark visited curr node
        
        for i in self.adj[curr]: # in curr node explore dfs
            
            if not self.dfs(i): 
                return False # if cycle exist
            
        self.visited[curr]=1 #processed
        self.ans.append(curr) # before backtrack add in ans
        
        return True
        
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        n = len(prerequisites)
        self.adj = defaultdict(list)
        self.ans = []
        
        for i in prerequisites:
            self.adj[i[0]].append(i[1])  # make graph
            
        self.visited = [0]*numCourses # visited arr , 0=>not visited, 1 -> completed 2->processing
        
        for i in range(numCourses):
            if not self.dfs(i): # start with any node and dfs until cycle
                return [] # if cycle return []
        return self.ans
            
        
            
            
        