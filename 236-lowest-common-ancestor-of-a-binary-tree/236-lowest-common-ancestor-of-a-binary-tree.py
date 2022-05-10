# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if(root==None or root==p or root==q):
            return root
        
        lans = self.lowestCommonAncestor(root.left,p,q)
        rans = self.lowestCommonAncestor(root.right,p,q)
        
        if(lans==None):
            return rans
        elif (rans==None):
            return lans
        else:
            return root
        