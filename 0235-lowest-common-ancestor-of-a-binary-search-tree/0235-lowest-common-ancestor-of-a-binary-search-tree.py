# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root is None:
            return root
        
        while(root):
            
            if root == p or root == q:
                return root
            
            elif (root.val >p.val and root.val > q.val):
                root = root.left
            
            elif (root.val < p.val and root.val < q.val):   
                root = root.right
            
            else:
                
                return root # p and q are both opposite side of root ,so root is lca
        
        
        return root
        