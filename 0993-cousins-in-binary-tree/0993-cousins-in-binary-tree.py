# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def checkSweetHomeAlabama(self,root,d,parent,x,y):
            
            if root is None:
                return
            
            if root.val==x:
                self.x = [d,parent]
                return
            
            if root.val==y:
                self.y = [d,parent]
                return
            
            self.checkSweetHomeAlabama(root.left,d+1,root,x,y)
            self.checkSweetHomeAlabama(root.right,d+1,root,x,y)
            
            return
    
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        if x==y:
            return False
    
        # stores depth and parent 
        self.x = [-1,None]
        self.y = [-1,None]
        
        self.checkSweetHomeAlabama(root,0,None,x,y)
        
        if self.x[0]!=-1 and self.x[0]==self.y[0] and self.x[1]!=self.y[1]: #check necessary conditions for being cousins
            return True
        
        return False
        
        
        