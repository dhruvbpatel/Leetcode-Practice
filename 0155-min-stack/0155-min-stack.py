class MinStack:

    def __init__(self):
        self.arr=list()
        self.temp=list()
        

    def push(self, val: int) -> None:
        
        self.arr.append(val)
        
        if len(self.temp)==0:
            self.temp.append(val)
        elif self.temp[-1]>val:
            self.temp.append(val)
        else:
            top = self.temp[-1]
            self.temp.append(top)
        

    def pop(self) -> None:
        self.arr.pop(-1)
        self.temp.pop(-1)
        

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.temp[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()