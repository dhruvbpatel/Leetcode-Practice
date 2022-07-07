class TimeMap:

    def __init__(self):
        self.d = {} # dict of key:[list]
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d.keys():
            self.d[key] = [] ##initialize key with list
        self.d[key].append([value,timestamp]) #add list in val
        
        # it is mentioned that new values are in increasing timestamp, i.e already sorted

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        
        values = self.d.get(key,[]) #get values list of current key, if empty return " "
        
        l = 0
        r = len(values)-1
        
        while l<=r:
            
            mid = (l+r)//2
            
            # if curr timestamp is greater than given timestamp then no use
            if values[mid][1]<=timestamp:
                ans = values[mid][0]
                l = mid+1
            else:
                r = mid-1
        return ans
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)