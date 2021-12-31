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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        
        
         if(!l1){
                return l2;
            }       
        
            else if(!l2){
                return l1;
            }
            
        
        // else if(l1->val < l2->val){
        //     l1->next = mergeTwoLists(l1->next,l2);
        //     return l1;
        // }else{
        //     l2->next = mergeTwoLists(l1,l2->next);
        //     return l2;
        // }
        
        ListNode* temp  = new ListNode(-1);
        ListNode* head = temp;
        
        while(l1 and l2){
            if(l1->val<=l2->val){
                temp->next=l1;
                l1 = l1->next;
            }else{
                temp->next = l2;
                l2 = l2->next;
            }
            
            temp = temp->next;
        }
        
        if(l1){
            temp->next= l1;
            // l1 = l1->next;
            // temp = temp->next;
            
        }
        
        if(l2){
            temp->next = l2;
            // l2 = l2->next;
            // temp = temp->next;
        }
        
        
        return head->next;
        
           
            
            
        
    }
};