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
    
    int helper(TreeNode* root,int& maxsum){
        
        if(root==NULL){
            return 0;
        }
        
        int lsum = max(0,helper(root->left,maxsum));  // if lsum is -ve we ignore that as it is not helpful in finding maxsum
        int rsum = max(0,helper(root->right,maxsum));
        
        maxsum = max(maxsum,lsum+rsum+root->val);
        
        return max(lsum,rsum)+root->val;  // it return helps in choosing max path for each node 
        // i.e where to take lsum -> left path or rsum -> right path
        
    }
    
    int maxPathSum(TreeNode* root) {
        
        int maxsum = INT_MIN;
        
        int ans=helper(root,maxsum);
        
        return maxsum;
        
        
        
    }
};