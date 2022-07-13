# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = []
        
        q = []
        
        if root:
            q.append(root)
            
        
        while len(q)!=0:
            
            n = len(q)
            ans.append([])
            
            for i in range(n):
                
                curr = q.pop(0)
                
                ans[-1].append(curr.val)
                
                if curr.left:
                    q.append(curr.left)
                
                if curr.right:
                    q.append(curr.right)
        
        return ans
            
            
        
        