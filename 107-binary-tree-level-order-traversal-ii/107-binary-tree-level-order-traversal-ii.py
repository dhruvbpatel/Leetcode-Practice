# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return root
        
        q=[]
        ans = []
        
        q.append(root)
        
        while len(q):
            
            n = len(q)
            temp = []
            
            for i in range(n):
                
                curr = q[0]
                q.pop(0)
                
                # print(curr.val)
                
                temp.append(curr.val)
                
                if curr.left:
                    q.append(curr.left)
                
                if curr.right:
                    q.append(curr.right)
            
            # print(temp)
            ans.insert(0,temp)
        
        return ans
                
                
                
            