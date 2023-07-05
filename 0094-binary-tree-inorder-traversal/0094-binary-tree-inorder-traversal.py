# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        #morris traversal
        curr = root
        ans = []
        
        while curr:
            if curr.left is None:
                ans.append(curr.val)
                curr = curr.right
            
            else:
                
                predecessor = curr.left
                while predecessor.right:
                    predecessor =  predecessor.right
                
                predecessor.right = curr
                temp = curr
                curr = curr.left
                temp.left = None
            
        return ans
                
        
        
        