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
    int countNodes(TreeNode* root) {
//         if(root==NULL){
//             return 0;
//         }
        
//         int sum =0;
        
//         return sum+=countNodes(root->left)+countNodes(root->right)+1;
        
        
        if(root==NULL) return 0;
        
        int lh = leftHeight(root);
        int rh = rightHeight(root);
        
        if(lh==rh) return (1<<lh)-1;
        
        return 1+countNodes(root->left)+countNodes(root->right);
        
        
    }
    
    int leftHeight(TreeNode* root){
        int ht = 0;
        while(root){
            ht++;
            root = root->left;
        }
        return ht;
    }
    
    int rightHeight(TreeNode* root){
        int ht = 0;
        while(root){
            ht++;
            root = root->right;
        }
        return ht;
    }
    
    
};