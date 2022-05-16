# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        to_delete = set(to_delete)  # set containing node to be deleted
        
        # bottom up recursion
        def helper(node):
            
            if not node:
                return None
        
            node.left = helper(node.left)
            node.right = helper(node.right)
            
            if node.val in to_delete:
                
                if node.left:
                    ans.append(node.left)
                
                if node.right:
                    ans.append(node.right)
                return None
            
            return node
        
        
        helper(root) # dfs 
        
        if root.val not in to_delete:
            ans.append(root)
        
        return ans
            
        