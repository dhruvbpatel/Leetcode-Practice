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
        
        while(fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
        
        #slow at end of 1st half
        # reverse 2nd half
        
        second_start = self.reverse(slow.next)
        
        p1 = head
        p2 = second_start
        
        ans = True
        
        while(ans and p2!=None):
            if(p1.val!=p2.val):
                return False
            p1 = p1.next
            p2 = p2.next
        
        
        # slow.next = self.reverse(second_start)
        
        return True
        
        
        
        
        