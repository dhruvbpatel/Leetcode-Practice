# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isSame(self,root,s):
        
        if not root or not s:  
            return root==s # return true if both are same else false
        
        # condition to check same
        return root.val==s.val and self.isSame(root.left,s.left) and self.isSame(root.right,s.right)
    
    
    def isSubtree(self, root: Optional[TreeNode], s: Optional[TreeNode]) -> bool:
        
        if not root:  # if no root return false
            return False

        if not s: # if s is null, means it still exist in main tree
            return True
        
        if self.isSame(root,s): #check same
            return True
        
        return self.isSubtree(root.left,s) or self.isSubtree(root.right,s) # if not found check on left and right
        