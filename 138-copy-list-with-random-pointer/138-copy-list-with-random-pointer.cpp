/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
       
        
        Node* iter = head;
        Node* front = head;
        
        // step 1: create copies and attach
        
        
        while(iter!=NULL){
            front = iter->next;
            
            Node* n = new Node(iter->val);
            
            iter->next = n;
            n->next = front;
            iter = front;
        }
        
        
        // step 2: assign random pointer to copy
        
        
        iter = head;
        
        while(iter!=NULL){
            
            if(iter->random!=NULL){
                iter->next->random = iter->random->next;
                
            }
            
            iter = iter->next->next;
        }
        
        
        // step 3: detach ll
        
        iter = head;
        Node* dummy = new Node(0);
        Node* temp = dummy;
        
        while(iter!=NULL){
            
            front = iter->next->next;
            
            temp->next = iter->next;
            
            iter->next = front;
            
            temp= temp->next;
            
            iter = front;
            
        }
        
        return dummy->next;
        
    }
};