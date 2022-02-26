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
class BSTIterator {
    
        private: stack<TreeNode*> st;
        
        private:
                void pushLeft(TreeNode* node){

                    while(node!=NULL){
                        st.push(node);
                        node = node->left;
                    }

                }
public:
    
    
    
    BSTIterator(TreeNode* root) {
        pushLeft(root);  
    }
    
   
    
    int next() {
        
            TreeNode* curr = st.top();
            st.pop();
            pushLeft(curr->right);
            return curr->val;
        
        // return ans;
            
    
        
    }
    
    bool hasNext() {
        return !st.empty();
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */