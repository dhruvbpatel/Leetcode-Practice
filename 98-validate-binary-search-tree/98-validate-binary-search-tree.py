# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys

class Solution:
    
    def check(self,root,mn,mx):
        
        if root is None:
            return True
        
        if root.val <=mn or root.val >=mx:
            return False
        
        if self.check(root.left,mn,root.val) and self.check(root.right,root.val,mx):
            return True
        
        return False
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.check(root,-1*sys.maxsize-1,sys.maxsize)
    
        