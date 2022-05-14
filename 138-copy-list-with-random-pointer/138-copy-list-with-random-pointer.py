"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        curr = head
        nxt = head
        
        while(curr):
            nxt = curr.next
            newnode = Node(curr.val,None,None)
            curr.next = newnode
            newnode.next = nxt
            curr = nxt
        
        
        curr = head
        
        while(curr):
            if(curr.random is not None):
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        dummy = ListNode(-1)
        temp = dummy
        curr = head
        
        
        while(curr):
            nxt = curr.next.next
            temp.next = curr.next
            curr.next = nxt
            temp = temp.next
            curr = nxt
        
        return dummy.next
            
            
        
        
            
        
        
        