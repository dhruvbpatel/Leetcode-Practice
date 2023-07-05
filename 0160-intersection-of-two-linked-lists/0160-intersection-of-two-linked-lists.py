# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        if(headA is None or headB is None):
            return None
    
        h1 = headA
        h2 = headB
        
        while(h1 != h2):
            h1 = headB if h1 is None else h1.next
            h2 = headA if h2 is None else h2.next
        
        return h1