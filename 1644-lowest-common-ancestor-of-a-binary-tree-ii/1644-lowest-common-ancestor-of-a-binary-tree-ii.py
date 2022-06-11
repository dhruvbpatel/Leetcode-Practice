# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def helper(self,root,p,q):
        
        if root==None:
            return root
        
        lans = self.helper(root.left,p,q)
        rans = self.helper(root.right,p,q)
        
        
        if root == p or root==q:
            self.count_node+=1
            return root
            

        if lans is None:
            return rans
        elif rans is None:
            return lans
        else:
            return root
        
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.count_node = 0
        
        ans = self.helper(root,p,q)
        
        if(self.count_node==2):
            return ans
        else:
            return None
        
        
        
        