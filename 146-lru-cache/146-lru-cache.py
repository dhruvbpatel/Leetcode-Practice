class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        

class LRUCache:

    def __init__(self, capacity: int):
        self.mp = dict()
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        

    def get(self, key: int) -> int:
        if key in self.mp:
            node = self.mp[key]
            self.removeNode(node)
            self.insertHead(node)
            return node.value
        else:
            return -1
    
    def removeNode(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insertHead(self,node):
        headnext = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = headnext
        headnext.prev = node
    
    def removeTail(self):
        if len(self.mp)==0: return
        tailnode = self.tail.prev
        del self.mp[tailnode.key]
        self.removeNode(tailnode)
        
        
    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            node = self.mp[key]
            self.removeNode(node)
            self.insertHead(node)
            node.value = value
        else:
            if len(self.mp) >=self.capacity:
                self.removeTail()
            node = Node(key,value)
            self.mp[key] = node
            self.insertHead(node)
            
            
            
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)