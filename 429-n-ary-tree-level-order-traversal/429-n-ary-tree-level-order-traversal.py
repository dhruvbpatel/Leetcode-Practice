"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if not root:
            return []
        
        ans = []
        
        q = []
        
        q.append(root)
        
        while len(q):
            
            n = len(q)
            temp = []
            
            for i in range(n):
                
                curr = q.pop(0)
                temp.append(curr.val)
                
                for child in curr.children:
                    q.append(child)
            
            
            ans.append(temp)
        
        
        return ans
                    
                    
                    
        
        
        
        
        
        
        
        
        
        
        