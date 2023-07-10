"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        visited = {}
        
        def clone(node):
            
            if node in visited:
                return visited[node]
            
            cloneNode = Node(node.val)
            visited[node]=cloneNode
            
            for n in node.neighbors:
                cloneNode.neighbors.append(clone(n))
            
            return cloneNode
        
        return clone(node) if node else None