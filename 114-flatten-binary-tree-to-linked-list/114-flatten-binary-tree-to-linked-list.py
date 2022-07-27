# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def solve(self,root):
        
        if root is None:
            return None
        
        if root.left is None and root.right is None:
            return root
        
        leftTail = self.solve(root.left) #get left tail recursively
        rightTail = self.solve(root.right) #get right tail reursively
        
        
        if leftTail:
            leftTail.right = root.right  #connect leftend to root.right
            root.right = root.left #swap left to right
            root.left = None #now was leftail connect to right head make left None
        
        return rightTail if rightTail else leftTail #final check and return
        
        
        
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        self.solve(root)
        
        