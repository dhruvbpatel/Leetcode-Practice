# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return None
        
        q = []
        ans = []
        
        q.append(root)
        
        while(len(q)!=0):
            
            s = len(q)
            
            for i in range(s):
                
                curr = q[0]
                q.pop(0)
                
                if(i==s-1):
                    ans.append(curr.val)
                
                if(curr.left):
                    q.append(curr.left)
                
                if(curr.right):
                    q.append(curr.right)
        
        return ans
        