# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self,root):
        if root is None:
            return root
        l = self.helper(root.left)
        r = self.helper(root.right)
        
        root.left = r
        root.right =l
        
        return root
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        self.helper(root)
        return root
      