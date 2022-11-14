# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self,root,mxsum):
        
        if root is None:
            return 0
        
        lsum = max(0,self.helper(root.left,self.mxsum))
        rsum = max(0,self.helper(root.right,self.mxsum))
        
        self.mxsum = max(self.mxsum,root.val+lsum+rsum) #max value for path including root
        
        return max(lsum,rsum)+root.val #return sum of root + only one child as we can't includde both as that won't be valid path
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.mxsum = -100001
        
        self.helper(root,self.mxsum)
        
        return self.mxsum
    
    
    