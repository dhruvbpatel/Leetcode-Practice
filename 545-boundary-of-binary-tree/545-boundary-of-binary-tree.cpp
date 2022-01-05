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
    
    bool isLeaf(TreeNode* root){
        
        if(root==NULL) return false;
        
        if(root->left==NULL and root->right==NULL){
            return true;
        }
        return false;
    }
    
    void addLeftBoundary(TreeNode* root,vector<int>& ans){
        TreeNode* curr = root->left;
        
        while(curr){
            if(!isLeaf(curr)) ans.push_back(curr->val);
            
            if(curr->left) curr = curr->left;
            else curr = curr->right;
        }
    }
    
    
    void addLeaves(TreeNode* root,vector<int>& ans){
        
        if(isLeaf(root)){
            ans.push_back(root->val);
            return;
        }
        
        if(root->left) addLeaves(root->left,ans);
        if(root->right) addLeaves(root->right,ans);
        
        
    }
    
    void addRightBoundary(TreeNode* root,vector<int>& ans){
        
        TreeNode* curr = root->right;
        vector<int> temp;
        
        while(curr){
            if(!isLeaf(curr)) temp.push_back(curr->val);
            
            if(curr->right) curr=curr->right;
            else curr = curr->left;
        }
        
        for(int i=temp.size()-1;i>=0;i--){
            ans.push_back(temp[i]);
        }
        
        
    }
    
    vector<int> boundaryOfBinaryTree(TreeNode* root) {
        
        vector<int> ans;
        
        if(!root) return ans;
        
        if(!isLeaf(root)) ans.push_back({root->val}); // 1st add root to ans;
        
        addLeftBoundary(root,ans);
        addLeaves(root,ans);
        addRightBoundary(root,ans);
        
        return ans;
        
        
    }
};