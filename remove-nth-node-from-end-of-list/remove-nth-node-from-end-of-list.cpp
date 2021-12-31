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
    
    int len(ListNode* head){
        int count =0;
        
        ListNode* temp = head;
        
        while(temp!=NULL){
            temp =temp->next;
            count++;
        }
        
        return count;
    }
    
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        
        if(head==NULL){
            return head;
        }
        
        int l = len(head);
        
        int target = l-n-1;
        
        
        if(n==l) return head->next;
        
        ListNode* curr = head;
        
        
        while(curr!=NULL and target--){
            curr = curr->next;
        }
        
        curr->next = curr->next->next;
        
        return head;
        
       
        
        
    }
};