/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    
    int length(ListNode* head){
        if(head==NULL){
            return 0;
        }
        
        int count= 0;
        
        ListNode* temp= head;
        
        while(temp!=NULL){
            temp = temp->next;
            count++;
        }
        
        return count;
    }
    
    ListNode *getIntersectionNode(ListNode *h1, ListNode *h2) {
        
            int l1 = length(h1);
            int l2 = length (h2);
        
            int d= 0;
        
            ListNode* p1;
            ListNode* p2;
        
            if(l1>l2){
                d = l1-l2;
                p1 = h1;
                p2 = h2;
                
            }else{
                d = l2-l1;
                p1 = h2;
                p2 = h1;
            }
            
            
        while(d--){
            
            if(p1==NULL){
                return NULL;
            }
            
            p1 = p1->next;
                
            
            
        }
        
        while(p1!=NULL && p2!=NULL){
            
            if(p1==p2){
                return p1;
            }
            
            p1 = p1->next;
            p2  = p2->next;
        }
        
        return NULL;
        
        
            
    }
};