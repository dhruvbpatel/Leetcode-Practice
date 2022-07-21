# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    nxt = None
    
    def reverseFirstN(self,head,n):
        self.nxt = None
        if n==1:
            self.nxt = head.next
            return head
        
        last = self.reverseFirstN(head.next,n-1)
        head.next.next=head
        head.next = self.nxt
        return last
        
    
    def reverseBetween(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        
        if m==1:
            return self.reverseFirstN(head,n)
        
        head.next = self.reverseBetween(head.next,m-1,n-1)
        
        return head
        
        