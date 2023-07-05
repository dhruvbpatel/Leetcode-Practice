# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
                
        q = []
        ans = []
        
        if root:
            q.append(root)
        
        while q:
            
            n = len(q)
            
            temp = []
            
            for i in range(len(q)):
                
                curr = q.pop(0)
                
                temp.append(curr.val)
                
                if curr.left:
                    q.append(curr.left)
                
                if curr.right:
                    q.append(curr.right)
            
            ans.append(temp)
        
        return ans
                
        
        