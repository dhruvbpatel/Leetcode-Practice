# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def get_length(self,head):
        temp = head
        count = 0
        while(temp):
            count+=1
            temp = temp.next
        return count
    
    def helper(self,head,l,k):
        
        if(l<k):
            return head
        
        curr=head
        prev = None
        count = 0
        nxt = None
        while(curr is not None and count<k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            count+=1
        
        if(nxt):
            head.next = self.helper(nxt,l-k,k)
        
        return prev
        
            
        
        
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = self.get_length(head)
        return self.helper(head,l,k);
        