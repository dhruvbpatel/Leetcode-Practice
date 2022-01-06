/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    
    void mark_parent(TreeNode* root, TreeNode* target,unordered_map<TreeNode*, TreeNode*>& parent_track){
        
        queue<TreeNode*> q;
        q.push(root);
        
        while(!q.empty()){
            TreeNode* curr = q.front();
            q.pop();
            
            if(curr->left){
                parent_track[curr->left] = curr; // add in map
                q.push(curr->left);
            }
            
            if(curr->right){
                parent_track[curr->right] = curr; // add in map
                q.push(curr->right);
            }
            
        }
        
    }
    
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        
        unordered_map<TreeNode*,TreeNode*> parent_track;
        
        mark_parent(root,target,parent_track);  // mark in parent
        
        unordered_map<TreeNode*,bool> visited;
        
        queue<TreeNode*> q;
        
        q.push(target);
        
        visited[target] = true; // mark target visited;
        
        int curr_level = 0;
        
        while(!q.empty()){
            
            int n = q.size();
            
            if(curr_level++ == k) break; // while we traver to distance k do it , we reach k level break of while loop
            
            for(int i=0;i<n;i++){
                TreeNode* curr = q.front();
                q.pop();
                
                if(curr->left and !visited[curr->left]){ // visit left;
                    q.push(curr->left);
                    visited[curr->left] = true;
                }
                
                if(curr->right and !visited[curr->right]){  // visit right
                    q.push(curr->right);
                    visited[curr->right] = true;
                }
                
                if(parent_track[curr] and !visited[parent_track[curr]]){  // check parent;
                    q.push(parent_track[curr]);
                    visited[parent_track[curr]]=true;
                }
                
            }
            
        }
        
        vector<int> ans;
            // k=2 so now all in q are our ans at k distance;
            while(!q.empty()){
                TreeNode* curr = q.front();
                q.pop();
                ans.push_back(curr->val);
            }
        return ans;
        
        
    }
};