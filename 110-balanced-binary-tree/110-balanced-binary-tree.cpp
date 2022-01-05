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
    
    bool helper(TreeNode* root, int* height){
        if(root==NULL){
            *height = 0;
            return true;
        }
        
        int lh = 0,rh = 0;
        
        if(helper(root->left,&lh)==false){
            return false;
        }
        
        if(helper(root->right,&rh)==false){
            return false;
        }
        
        *height = max(lh,rh)+1;
        
        if(abs(lh-rh)<=1){
            return true;
        }else{
            return false;
        }
        
    }
    
    int dfsHeight(TreeNode* root){
        
        if(root==NULL){
            return 0;
        }
        
        int lh = dfsHeight(root->left);
        
        if(lh==-1) return -1;
        
        int rh = dfsHeight(root->right);
        
        if(rh==-1) return -1;
        
        if(abs(rh-lh)>1) return -1;
        
        return max(rh,lh)+1;
        
    }
    
    bool isBalanced(TreeNode* root) {
        
        // int height = 0;
        // return helper(root,&height);
        return dfsHeight(root)!=-1;       
    }
};