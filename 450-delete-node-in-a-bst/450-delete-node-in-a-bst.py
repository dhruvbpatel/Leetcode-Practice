# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # to merge tree after deletion
    def helper(self,root):
        
        if root.left is None:
            return root.right
        
        elif root.right is None:
            return root.left
        
        rightNode = root.right
        lastRight = self.findLastRight(root.left)
        lastRight.right = rightNode
        return root.left
    
    
    ## get last right
    def findLastRight(self,root):
        
        if root.right is None:
            return root
        
        return self.findLastRight(root.right)
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if root is None:
            return root
        
        if root.val == key:
            return self.helper(root)
        
        dummy = root
        
        while root:
            
            if root.val > key: ## go to left
                
                if root.left != None and root.left.val == key:
                    root.left = self.helper(root.left)
                    break
                else:
                    root = root.left
            
            else: #goto right
                
                if root.right !=None and root.right.val == key:
                    root.right = self.helper(root.right)
                    break
                else:
                    root = root.right
                
        return dummy

        