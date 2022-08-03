class Node:
    
    def __init__(self,start,end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class MyCalendar:

    def __init__(self):
        self.root = None
    
    def buildTree(self,start,end,node):
        
        if start>=node.end:
            if node.right:
                return self.buildTree(start,end,node.right)
            
            else:
                node.right = Node(start,end)
                return True
        
        elif end<=node.start:
            
            if node.left:
                return self.buildTree(start,end,node.left)
            else:
                node.left = Node(start,end)
                return True
        else:
            
            return False
            
        
    def book(self, start: int, end: int) -> bool:
        
        if not self.root:
            self.root = Node(start,end)
            return True
        
        return self.buildTree(start,end,self.root)

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)