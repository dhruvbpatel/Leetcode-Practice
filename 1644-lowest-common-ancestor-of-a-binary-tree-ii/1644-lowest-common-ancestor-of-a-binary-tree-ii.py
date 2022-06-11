# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def helper(self,root,p,q):
        
        if root==None: #if root is none return
            return root
        
        ##iterate over all nodes
        lans = self.helper(root.left,p,q)
        rans = self.helper(root.right,p,q)
        
        #if root is p or root is q ,update count of nodes and return node
        if root == p or root==q:
            self.count_node+=1
            return root  ## here we return because if 2nd node is descendant of current node then curr is LCA
            
        
        if lans is None:
            return rans
        elif rans is None:
            return lans
        else:
            return root
        
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.count_node = 0  ## to check if both nodes are found
        
        ans = self.helper(root,p,q)
        
        if(self.count_node==2): #if only both are found return ans
            return ans
        else:
            return None # else none
        
        
        
        