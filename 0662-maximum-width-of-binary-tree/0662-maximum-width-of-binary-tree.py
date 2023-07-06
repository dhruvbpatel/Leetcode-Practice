# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
    
        ans = 0
        
        q = [(root,0)]
        
        while len(q)!=0:
            first=0
            last=0
            n = len(q)
            mmin = q[0][1] # to make id for each level start from  0 to avoid overflowing we take lowest id in each level
            
            for i in range(n):
                curr_id = q[0][1]-mmin
                node = q[0][0]
                
                q.pop(0)
                
                if i==0:
                    first = curr_id
                
                if i==n-1:
                    last = curr_id
                
                if node.left:
                    q.append((node.left,2*curr_id+1))
                
                if node.right:
                    q.append((node.right,2*curr_id+2))
            
            ans = max(ans,last-first+1)
        
        return ans