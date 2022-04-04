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
    ListNode* swapNodes(ListNode* head, int k) {
        
        ListNode* curr = head;
        ListNode* end = NULL;
        ListNode* front = NULL;
        
        int l = 0;
        
        while(curr){ // iterate curr node
            l++;
            
            if(end!=NULL){
                end = end->next;  // itearate end as well until not null
            }
            
            // end node would be k position behind when curr node reached end, i.e kth position from end;
            
            if(l == k){  // if lenght ==k we have reached front node, mark front and reset end
                front = curr;
                end = head;
            }
            
            curr = curr->next;  // increase curr at each step;
        }
        
        swap(front->val,end->val); // swap val at end
        return head;
    }
};