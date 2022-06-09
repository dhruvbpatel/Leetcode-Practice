# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    
    def helper(self,root,mxsum):
        
        if root is None:
            return 0
        
        lsum = max(0,self.helper(root.left,self.mxsum))
        rsum = max(0,self.helper(root.right,self.mxsum))
        
        self.mxsum = max(self.mxsum,lsum+rsum+root.val)
        
        return max(lsum,rsum)+ root.val
        
    
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.mxsum = -10001
        
        ans = self.helper(root,self.mxsum)
        
        return self.mxsum
        
        