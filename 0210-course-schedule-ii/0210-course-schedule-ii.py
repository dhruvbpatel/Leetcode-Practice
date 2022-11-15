from collections import defaultdict

class Solution:
    
    
    def isCycle(self,curr):
        
        if(self.visited[curr]==2): # mark processing
            return True # cycle detected
        
        if(self.visited[curr]==1):
            return False  # already processed, and added to ans
        
        self.visited[curr]=2 # mark visited curr node
        
        for i in self.adj[curr]: # in curr node explore dfs
            
            if self.isCycle(i): 
                return True # if cycle exist
            
        self.visited[curr]=1 #processed
        self.ans.append(curr) # before backtrack add in ans
        
        return False
        
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        n = len(prerequisites)
        self.adj = defaultdict(list)
        self.ans = []
        
        for i in prerequisites:
            self.adj[i[0]].append(i[1])  # make graph
            
        self.visited = [0]*numCourses # visited arr , 0=>not visited, 1 -> completed 2->processing
        
        for i in range(numCourses):
            if self.isCycle(i): # start with any node and dfs until cycle
                return [] # if cycle return []
        return self.ans
            
        
            
            
        