class ProductOfNumbers:
    
     # Purpose: imp. product of the last k numbers in an array
    # Method: 
    # Intuition: obtain cumulative product from end to start with zero-restart
    
    # Explanation: 
    # Action    Arr              cur             self.pro
    # add(3)    [3]              [1*3=3]         [3] # append
    # add(0)    [3,0]            [1]             [1] # restart
    # add(2)    [3,0,2]          [1*2=2]         [1,2] # append
    # add(5)    [3,0,2,5]        [2*5=10]        [1,2,10] # append
    # add(4)    [3,0,2,5,4]      [10*4=40]       [1,2,10,40] # append

    def __init__(self):
        
        self.prefix  = [1]
        
        

    def add(self, num: int) -> None:
        
        if num==0:
            #reset prefix
            self.prefix = [1]
        
        else:
            
            curr = self.prefix[-1]*num
            self.prefix.append(curr)
        

    def getProduct(self, k: int) -> int:
        
        #we can see we sometimes reset our prefix, so in this we have a range of last k products which are non zero
        # so if k>=len(self.prefix) it means we are searching out of range i.e there would be zero multiplication at that k
        # and after which we reset prefix to [1]. 
        # so if out of range k , means last k products is 0
        
        if k>=len(self.prefix):
            return 0
        
        #if k is in our range
        # we have all prefix to last k products
        
        #slicing to get desired k range product
        return self.prefix[-1]//self.prefix[-1-k]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)