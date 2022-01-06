/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void helper(TreeNode* root,int& k, priority_queue<int>& pq){
        
        if(root==NULL){
            return;
        }
        
        pq.push(root->val);
        if(pq.size()>k){
            pq.pop();
        }
        
        if(root->left){
            
            
            helper(root->left,k,pq);
        }
        
        if(root->right){
            
            
            helper(root->right,k,pq);
            
        }
        
//         if(root->left==NULL and root->right==NULL){
            
//             pq.push(root->val);
            
//             if(pq.size()>k){
//                 pq.pop();
//             }
            
//             // return;
//         }
        
    }
    
    int kthSmallest(TreeNode* root, int k) {
        
        if(root->left==NULL and root->right==NULL){
            return root->val;
        }
        
        priority_queue<int> pq;
        helper(root,k,pq);
        return pq.top();
    }
};