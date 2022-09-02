# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        if not root:
            return None
        
        q =[]
        
        q.append(root)
        
        ans =[]
        
        while len(q):
            
            n = len(q)
            
            temp = 0
            
            for i in range(n):
                curr = q.pop(0)
                
                temp+=curr.val
                
                if curr.left:
                    q.append(curr.left)
                
                if curr.right:
                    q.append(curr.right)
            
            
            ans.append(temp/n)
        
        return ans
            
            
        