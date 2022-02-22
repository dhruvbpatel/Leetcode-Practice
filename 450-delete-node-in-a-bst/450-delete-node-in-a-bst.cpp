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
    TreeNode* deleteNode(TreeNode* root, int key) {
        
        if(root==NULL) return root;
        
        if(root->val==key) return helper(root); // if root is to be deleted
        
        TreeNode* curr = root;
        
        // search key in bst
        while(root){
            if(root->val>key){ // in left half;
                if(root->left!=NULL and root->left->val==key){ // check if left node is our key
                    root->left = helper(root->left); // if yes delete
                    break;
                }else{ // if no search further 
                    root = root->left;
                }
            }else{ // in right half;
                if(root->right!=NULL and root->right->val==key){
                    root->right = helper(root->right);
                    break;
                }else{
                    root = root->right;
                }
            }
        }
        
        return curr;
        
        
    }
    
    TreeNode* helper(TreeNode* root){
        if(root->left==NULL) return root->right;
        if(root->right==NULL) return root->left;
        
        TreeNode* rightchild = root->right;
        TreeNode* lastRightInLeft = findLastRight(root->left);
        lastRightInLeft->right  = rightchild;
        return root->left;
        
    }
    
    TreeNode* findLastRight(TreeNode* root){
        if(root->right == NULL){
            return root;
        }
        return findLastRight(root->right);
    }
    
};