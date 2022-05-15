# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverse(self,head):
        
        curr = head
        prev = None
        
        while(curr):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if head is None or head.next is None:
            return True
        
        fast = head
        slow = head
        
        # if fast reaches last or second last
        while(fast.next!=None and fast.next.next!=None):
            slow = slow.next
            fast = fast.next.next
        
        #slow at end of 1st half
        # reverse 2nd half
        
        second_start = self.reverse(slow.next)
        
        p1 = head
        p2 = second_start # p2's end is not pointing to null, so linkedlist is broken in a sense
        
        # ans = True
        
        while(p2 is not None):
            if(p1.val!=p2.val):
                return False
            
            p1 = p1.next
            p2 = p2.next
        
        
        # while(ans and p2!=None):
        #     if(p1.val!=p2.val):
        #         return False
        #     p1 = p1.next
        #     p2 = p2.next
        
        
        slow.next = self.reverse(second_start)
        
        return True
        
        
        
        
        