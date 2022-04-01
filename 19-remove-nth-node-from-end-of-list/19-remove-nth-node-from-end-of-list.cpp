/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        
        // optimized solution ->  no need to use length loop
        
        ListNode* dummy = new ListNode(-1); // create dummy node
        dummy->next = head;
        ListNode* fast = dummy; // 2 pointers
        ListNode* slow = dummy;
        
        for(int i=0;i<n;i++){ // move fast n times
            fast = fast->next;
        }
        
        while(fast->next!=NULL){ // until fast reaches last node move both 
            fast=fast->next;
            slow = slow->next;
        }
        
        slow->next = slow->next->next;  // slow is at desired position , remove slow->next
        return dummy->next; return head;
        
    }
};