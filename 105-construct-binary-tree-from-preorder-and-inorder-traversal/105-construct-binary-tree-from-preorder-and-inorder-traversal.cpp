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
    
    TreeNode* helper(vector<int>& preorder, vector<int>& inorder,int& idx,int start,int end){
        
        if(start>end){
            return NULL;
        }
        
        int pos = start;
        
        while(inorder[pos]!=preorder[idx]){
            pos++;
        }
        
        idx++;
        
        TreeNode* node = new TreeNode(inorder[pos]);
        
        node->left = helper(preorder,inorder,idx,start,pos-1);
        node->right = helper(preorder,inorder,idx,pos+1,end);
        
        return node;
        
        
    }
    
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
              
        int idx = 0;
        return helper(preorder,inorder,idx,0,inorder.size()-1);
    }
};