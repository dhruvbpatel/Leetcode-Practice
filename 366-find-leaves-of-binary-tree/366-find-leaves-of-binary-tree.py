# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root):
        if root is None:
            return 0
        
        d = max(self.dfs(root.left),self.dfs(root.right))+1
        
        if(len(self.ans)<d):
            self.ans.append([])
        
        self.ans[d-1].append(root.val)
        return d
        
        
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = []
        self.dfs(root)
        return self.ans
    