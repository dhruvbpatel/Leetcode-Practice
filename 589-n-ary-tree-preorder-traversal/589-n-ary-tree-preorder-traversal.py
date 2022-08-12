"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    
    def solve(self,root,ans):
        
        if root is None:
            return None
        
        self.ans.append(root.val)
        
        if root.children:
            
            for child in root.children:
                
                self.solve(child,self.ans)
        return
    
    def preorder(self, root: 'Node') -> List[int]:
        
        self.ans = []
        
        self.solve(root,self.ans)
        return self.ans
            
            
        
        
        