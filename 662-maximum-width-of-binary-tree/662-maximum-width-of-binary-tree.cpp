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
    int widthOfBinaryTree(TreeNode* root) {
        
        if(root==NULL) return 0;
        
        int ans =0;
        
        queue<pair<TreeNode*,int>> q;
        q.push({root,0}); // node,indexing (level wise indexing starring iwth 1-2-3...2^(level no);
        
        while(!q.empty()){ // we travel level oder wise
            
            int n = q.size();
            int min_idx = q.front().second; // get the min indexing of curr level;
            int first,last;
            
            for(int i=0;i<n;i++){
                
                TreeNode* curr = q.front().first;
                int curr_idx = q.front().second-min_idx;
                q.pop();
                
                if(i==0) first = curr_idx;
                if(i==n-1) last = curr_idx;
                
                if(curr->left){
                    q.push({curr->left,2*curr_idx+1});
                }
                
                if(curr->right){
                    q.push({curr->right,2*curr_idx+2});
                }
                
                
            }
            
            ans = max(ans,last-first+1);
        }
        
        return ans;
        
    }
    
};