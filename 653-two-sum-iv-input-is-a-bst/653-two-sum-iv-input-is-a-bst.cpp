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
    void inorder(vector<int>& io,TreeNode* root){
        if(root==NULL){
            return;
        }
        
        inorder(io,root->left);
        io.push_back(root->val);
        inorder(io,root->right);
    }
    
    bool findTarget(TreeNode* root, int k) {
        vector<int> io;
        
        inorder(io,root);
        
        int l= 0,r=io.size()-1;
        
        while(l<r){
            if(io[l]+io[r]==k){
                return true;
            }else if(io[l]+io[r]>k){
                r--;
            }else{
                l++;
            }
        }
        
        return false;
        
    }
};