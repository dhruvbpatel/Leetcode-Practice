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
    ListNode* swapPairs(ListNode* head) {
        
        if(!head or !head->next) return head;
        
        ListNode* curr = head;
        ListNode* front = head->next;
        
        curr->next = swapPairs(front->next); // all nodes ahead of front will be swapped
        front->next = curr; //  curr ->next here will have reversed score so we reverse front and curr;
        
        
        return front;
        
        
        
    }
};