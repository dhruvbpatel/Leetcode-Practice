class MaxStack:

    def __init__(self):
        self.stack = []
        self.max_stack = []
        
        

    def push(self, x: int) -> None:
        
        self.stack.append(x)
        
        ## only push in maxstack when change in max occurs or when its empty
        
        if not self.max_stack or x>=self.max_stack[-1]:
            self.max_stack.append(x)
        
        

    def pop(self) -> int:
        # if we are popping max element pop in maxstack as well
        
        if self.stack[-1] == self.max_stack[-1]:
            self.max_stack.pop()    
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def peekMax(self) -> int:
        if self.max_stack:
            return self.max_stack[-1]
        

    def popMax(self) -> int:
        
        
        
        temp = []
        
        ## find max in stack, if found then pop
        while self.stack[-1]!=self.max_stack[-1]:
            temp.append(self.stack[-1])
            self.stack.pop()
            
        # now to get to 2nd max we pop maxstack only once
        
        ans = self.stack.pop()
        self.max_stack.pop()
        
        # add back all in temp
        while temp:
            self.push(temp[-1]) ##using push function
            temp.pop()
        
        return ans
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()