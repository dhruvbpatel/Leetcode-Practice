# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        def helper(root,d,parent):
            
            if root is None:
                return
            
            if root.val==x:
                self.x = [d,parent]
                return
            
            if root.val==y:
                self.y = [d,parent]
                return
            
            helper(root.left,d+1,root)
            helper(root.right,d+1,root)
            
            return
        
        
        if x==y:
            return False
    
        
        self.x = [-1,None]
        self.y = [-1,None]
        
        helper(root,0,None)
        
        if self.x[0]!=-1 and self.x[0]==self.y[0] and self.x[1]!=self.y[1]:
            return True
        
        return False
        
        
        