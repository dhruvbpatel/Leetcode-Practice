class MinStack:

    def __init__(self):
        self.st = []
        self.mn = []
        
    def push(self, val: int) -> None:
        
        if len(self.st)==0:
            
            self.mn.append(val)
            self.st.append(val)
            return
            
        else:
            
            self.st.append(val)
            
            if(val>=self.mn[-1]):
                self.mn.append(self.mn[-1])
            else:
                self.mn.append(val)
                
        
    def pop(self) -> None:
        
        self.st.pop()
        self.mn.pop()
        

    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        return self.mn[-1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()