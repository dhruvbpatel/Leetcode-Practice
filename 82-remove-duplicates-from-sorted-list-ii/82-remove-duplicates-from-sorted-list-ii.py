# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        newhead = ListNode(-1,head) #newhead.next ==head
        
        temp = newhead 
        
        while head:
            
            if head.next!=None and head.val==head.next.val: #if curr and next is duplicate
                
                # skip all duplicate
                while head.next!=None and head.val==head.next.val:
                    head = head.next
                
                # update links via using temp pointer
                temp.next = head.next
                
            
            else:
                #move temp ahead as no duplicate
                temp = temp.next
            
            head = head.next
        
        
        return newhead.next