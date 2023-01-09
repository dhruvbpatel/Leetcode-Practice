# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def solve(self,root,ans):
        
        if root is None:
            return
        
        ans.append(root.val)
        self.solve(root.left,ans)
        self.solve(root.right,ans)
        
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return None
        
        ans = []
        
        self.solve(root,ans)
        
        return ans