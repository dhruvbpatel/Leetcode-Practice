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
    
    // bool isBst(TreeNode* root, TreeNode* min , TreeNode* max){
        
//         if(root==NULL){
//             return true;
//         }
        
//         if(min && root->val<=min->val){
//             return false;
//         }
        
//         if(max and root->val >= max->val ){
//             return false;
//         }
        
        
//         bool left = isBst(root->left,min,root);
//         bool right = isBst(root->right,root,max);
        
//         return left and right;
        
//     }
    
    bool checkBST(TreeNode* node,long min, long max){
        if(node==NULL) return true;
        
        if(node->val<=min || node->val>=max)
            return false;
        
        if(checkBST(node->left,min,node->val) and checkBST(node->right,node->val,max)){
            return true;
        }
        return false;
        
    }
        
    bool isValidBST(TreeNode* root) {
        
        return checkBST(root,LLONG_MIN,LLONG_MAX);
        
        // return isBst(root,NULL,NULL);
        
    }
};