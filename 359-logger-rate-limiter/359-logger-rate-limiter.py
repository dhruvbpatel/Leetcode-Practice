class Logger:

    def __init__(self):
        self.mp = defaultdict()
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        
        #todo:
        # if message not in mp then add with t+10 and return true
        # if in message in mp then if ts >= mp[mesage] then return true , also update timestamp
        # else false
        
        if message not in self.mp:
            self.mp[message] = timestamp+10
            return True
        else:
            
            if self.mp[message] <= timestamp:
                self.mp[message] = timestamp+10
                return True
            else:
                return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)