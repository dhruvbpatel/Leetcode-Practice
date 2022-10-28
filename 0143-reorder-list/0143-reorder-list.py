# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        temp = head
        
        slow = head
        fast = head
        
        #get mid
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #slow is mid
        
        #reverse 2nd half
        
        prev=None
        nxt = None
        
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        start = head
        end = prev
        
        while end.next:
            temp = start.next
            start.next = end
            
            start = temp
            
            temp = end.next
            end.next = start
            end = temp
        
        
        