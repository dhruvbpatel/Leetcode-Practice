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
        int count = 0;
        
        ListNode* temp = head;
        
        while(temp!=NULL){
            temp = temp->next;
            count++;
        }
        
        return count;
    }
    
    ListNode* reverseKhelper(ListNode* head,int k ,int l){
        
        if(l<k){
            return head;
            
        }
        
        ListNode* prev= NULL;
        ListNode* curr = head;
        ListNode* nextptr;
        
        int count = 0;
        
        
        while(curr!=NULL && count<k){
            nextptr = curr->next;
            curr->next = prev;
            prev=curr;
            curr = nextptr;
            count++;
        }
        
        if(nextptr!=NULL){
               head->next = reverseKhelper(nextptr,k,l-k);
        }
        
        return prev;  // prev wil be our new head
     
    
        
    }
    
    
    ListNode* reverseKGroup(ListNode* head, int k) {
        
        int l = len(head);
        return reverseKhelper(head,k,l);
        
    }
};