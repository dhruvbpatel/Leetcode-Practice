# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = []
        
        q = []
        
        ltr = True
        
        if(root):
            q.append(root)
            
        while(len(q)!=0):
            
            n = len(q)
            temp = [0]*n
            
            for i in range(n):
                
                curr = q[0]
                q.pop(0)
                
                idx = i if ltr==True else n-i-1
                
                temp[idx] = curr.val
                
                if curr.left:
                    q.append(curr.left)
                
                if curr.right:
                    q.append(curr.right)
                
            ltr = False if ltr is True else True
            ans.append(temp)
        
        return ans
                
        