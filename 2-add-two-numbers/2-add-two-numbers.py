# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        total = 0
        
        newhead = ListNode(-1)
        temp = newhead
        
        while(l1 or l2 or carry):
            if(l1 is not None):
                total+=l1.val
                l1 = l1.next
            
            
            if(l2 is not None):
                total+=l2.val
                l2 = l2.next
            
            
            total+=carry
            carry = total//10
            
            newnode = ListNode(total%10)
            temp.next = newnode
            temp = newnode
            
            total = 0
        
        return newhead.next
            
        
        
        