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
    
    ListNode* swapNodes(ListNode* head, int k) {
        
        if(!head) return NULL;
        
        int n = len(head);
        
        if(n%2==1 and k==(n/2)+1) return head;
                
        ListNode* l=head;
        ListNode* r = head;
        
        int lcount = k-1;
        int rcount = n-k;
        
        while(lcount and rcount){
            l = l->next;
            r = r->next;
            
            lcount--;
            rcount--;
        }
        
        while(lcount){
            l = l->next;
            // r = r->next;
            lcount--;
        }
        
        while(rcount){
            // l = l->next;
            r = r->next;
            rcount--;
        }
        
        int temp = l->val;
        l->val = r->val;
        r->val = temp;
        
        
        return head;
    }
};