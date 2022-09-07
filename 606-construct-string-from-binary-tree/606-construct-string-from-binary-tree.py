# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        # base cases
        if root is None:
            return ''
        
        # if root is leafnode
        if root.left is None and root.right is None:
            return f'{root.val}'
        
        # if no right node, continue on the left without leaving () for the right
        if root.right is None:
            return f'{root.val}({self.tree2str(root.left)})'
        
        
        return f'{root.val}({self.tree2str(root.left)})({self.tree2str(root.right)})'