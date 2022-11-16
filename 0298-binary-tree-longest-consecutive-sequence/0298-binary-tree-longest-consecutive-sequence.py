# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self,node,parent,currlen):
        
        if node is None:
            return
        
        if parent!=None and node.val==parent.val+1:
            currlen = currlen+1
        else:
            currlen = 1
        
        self.mxlen = max(self.mxlen,currlen)
        
        self.helper(node.left,node,currlen)
        self.helper(node.right,node,currlen)
        
    
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        self.mxlen = 0
        
        self.helper(root,None,0)
        
        return self.mxlen
        