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
    ListNode* rotateRight(ListNode* head, int k) {
        
        if(head==nullptr) return head;
        
        vector<int> arr;
        
        ListNode* temp = head;
        
        while(temp){
            arr.push_back(temp->val);
            temp = temp->next;
        }
        
        int n = arr.size();
        k = k%n;
        
        if(n==1) return head;
        
        reverse(arr.begin(),arr.end());
        reverse(arr.begin(),arr.begin()+k);
        reverse(arr.begin()+k,arr.end());
        
        temp = head;
        int i=0;
        while(temp){
            temp->val = arr[i++];
            temp = temp->next;
        }
        
        return head;
        
        
        
    }
};