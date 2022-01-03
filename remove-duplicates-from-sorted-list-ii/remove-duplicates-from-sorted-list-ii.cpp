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
    ListNode* deleteDuplicates(ListNode* head) {
        
        // ListNode*  = head;
        // ListNode* nxt = head->next;
        ListNode* newhead = new ListNode(-1,head);
        // newhead = head;
        ListNode* temp = newhead;// stores the node before begining of duplicate nodes
        
    
        while(head){
            
            // if begin is duplicate
            if(head->next!=NULL and  head->val == head->next->val){
                    // skipp all duplicate
                while(head->next!=NULL and head->val == head->next->val){
                    head = head->next;
                }
                // connect temp with next;
                temp->next = head->next;
                
            }else{
                
                temp = temp->next;
                
            }
            
            head = head->next;
            
        }
        
        return newhead->next;
        
        
    }
};