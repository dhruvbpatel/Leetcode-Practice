# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self,root):
        if root:
            self.helper(root.left)
            self.k -=1
            if self.k  == 0:
                self.ans = root.val
                return
            
            self.helper(root.right)
            
        
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # inorder of bst is sorted
        
        self.k = k
        self.ans = 0
        self.helper(root)
        return self.ans
        