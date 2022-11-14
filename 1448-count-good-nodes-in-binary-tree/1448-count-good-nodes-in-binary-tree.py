# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self,root,currmax):
        
        if root is None:
            return
        
        if root.val>=currmax:
            self.good+=1
            currmax = max(currmax,root.val)

        self.helper(root.left,currmax)
        self.helper(root.right,currmax)
        
        return
            
        
    
    def goodNodes(self, root: TreeNode) -> int:
        
        if root is None:
            return None
        
        
        self.good = 0
        currmax = root.val
        self.helper(root,currmax)
        return self.good
        