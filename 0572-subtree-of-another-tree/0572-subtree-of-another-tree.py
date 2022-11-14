# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isSame(self,root,s):
        
        if root is None or s is None:
            return root==s
        
        return root.val==s.val and self.isSame(root.left,s.left) and self.isSame(root.right,s.right)
    
    
    def isSubtree(self, root: Optional[TreeNode], s: Optional[TreeNode]) -> bool:
        
        if not root:
            return False
        
        if not s:
            return True
        
        if self.isSame(root,s):
            return True
        
        return self.isSubtree(root.left,s) or self.isSubtree(root.right,s)
    
        