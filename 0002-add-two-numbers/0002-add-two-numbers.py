# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        total = 0
        carry = 0
        
        
        temp = ListNode(-1)
        head = temp
        
        while l1 or l2 or carry:
            
            curr = 0
            
            if l1:
                curr+=l1.val
                l1 = l1.next
            
            if l2:
                curr+=l2.val
                l2 = l2.next
            
            curr+=carry
            
            carry = curr//10
            
            newNode = ListNode(curr%10)
            
            temp.next = newNode
            temp = newNode
            
        
        return head.next