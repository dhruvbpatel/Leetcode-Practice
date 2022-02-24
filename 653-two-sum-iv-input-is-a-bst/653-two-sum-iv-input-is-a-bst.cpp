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
class BSTIterator{
    stack<TreeNode*> st;
    bool reverse = true;
    // reverse -> true -> before -> i.e opposite traversal of next; i.e end from inorder
    //reverse->false->next traversal i.e from start in inorder
    
    public:
    
    // BSTIterator(TreeNode* root,bool i)
    
    BSTIterator(TreeNode* root,bool isReverse){
        reverse = isReverse;
        pushAll(root);
    }
     /** @return whether we have a next smallest number */
    bool hasNext() {
        return !st.empty();
    }

    /** @return the next smallest number */
    int next() {
        TreeNode *tmpNode = st.top();
        st.pop();
        if(!reverse) pushAll(tmpNode->right);
        else pushAll(tmpNode->left);
        return tmpNode->val;
    }
    
    void pushAll(TreeNode *node) {
        for(;node != NULL; ) {
             st.push(node);
             if(reverse == true) {
                 node = node->right; 
             } else {
                 node = node->left; 
             }
        }
    }

    
    
};

class Solution {
public:
//     
    
    bool findTarget(TreeNode* root, int k) {
        // naive approach is to get inorder in array and search for 2 numbers;
        // optimized approach is to use modified version of BST Iterator';
        
        if(!root) return false; 
        BSTIterator l(root, false); 
        BSTIterator r(root, true); 
        
        int i = l.next(); 
        int j = r.next(); 
        while(i<j) {
            if(i + j == k) return true; 
            else if(i + j < k) i = l.next(); 
            else j = r.next(); 
        }
        return false; 
    }
};