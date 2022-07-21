# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    
    
    def reverseFirstN(self,head,n):
        self.nxt = None #nxt node
        
        if n==1: #if only one node is to be reverse then mark nxt and return
            self.nxt = head.next ##mark next , useful when backtracked
            return head
        
        last = self.reverseFirstN(head.next,n-1) # recursively reverse , returns lastnode
        head.next.next=head #original still connected
        head.next = self.nxt #now connect first node to n+1 node,i.e nxt
        return last # return last which is new head
        
    
    def reverseBetween(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        
        if head is None or m==n:
            return head
        
        if m==1:
            return self.reverseFirstN(head,n) ## if first pointer is 1st node,
        # this boils down to reverse first N nodes only
        
        head.next = self.reverseBetween(head.next,m-1,n-1) #if m!=1 then reduce them
        
        return head
        
        