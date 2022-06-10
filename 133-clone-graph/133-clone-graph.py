"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    
    def __init__(self):
        self.visited = {}
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if node is None: ## empty array
            return None

        if node in self.visited:
            return self.visited[node]
        
        clone_node = Node(node.val)
        
        self.visited[node] = clone_node ## add clone node to visited
        
        for n in node.neighbors:
            
            clone_node.neighbors.append(self.cloneGraph(n))
        
        return clone_node
        
        