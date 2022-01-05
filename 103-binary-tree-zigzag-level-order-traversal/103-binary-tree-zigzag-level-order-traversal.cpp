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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        
        vector<vector<int>> ans;
        
        queue<TreeNode*> q;
        
        if(!root) return ans;
        
        bool ltr = true;
        
        q.push(root);
        
        while(!q.empty()){
            
            int n = q.size();
            vector<int> row(n);
            
            for(int i=0;i<n;i++){
                
                TreeNode* curr = q.front();
                q.pop();
                
                int index = ltr ? i : (n-i-1);
                row[index] = curr->val;
                
                if(curr->left) q.push(curr->left);
                if(curr->right) q.push(curr->right);
            }
            
            ltr = !ltr;
            ans.push_back(row);
            
        }
                
        return ans;
        
    }
};