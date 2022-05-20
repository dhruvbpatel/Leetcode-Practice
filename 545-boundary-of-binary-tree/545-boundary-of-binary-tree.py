# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def addleaf(self,root,ans):
        
        if(self.isLeaf(root)):
            ans.append(root.val)
            return;
        
        if(root.left):
            self.addleaf(root.left,ans)
        
        if(root.right):
            self.addleaf(root.right,ans)
        
        
    
    def isLeaf(self,root):
        if root is None:
            return False
        
        if root.left is None and root.right is None:
            return True
        
        return False
    
    def addleft(self,root,ans):
        
        curr = root.left
        
        while(curr):
            
            if(self.isLeaf(curr)==False):
                ans.append(curr.val)
            
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right
        
    def addright(self,root,ans):
        
        temp = []
        
        curr = root.right
        
        while(curr):
            if(self.isLeaf(curr)==False):
                temp.append(curr.val)
            
            if(curr.right):
                curr = curr.right
            
            else:
                curr = curr.left
        # print(temp)
        ans.extend(temp[::-1])
        
    
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []
        
        if(root is None):
            return ans
    
        if(not self.isLeaf(root)):
            ans.append(root.val)
            
        self.addleft(root,ans)
        # print(ans)
        self.addleaf(root,ans)
        # print(ans)
        self.addright(root,ans)
        # print(ans)
        return ans
        
        