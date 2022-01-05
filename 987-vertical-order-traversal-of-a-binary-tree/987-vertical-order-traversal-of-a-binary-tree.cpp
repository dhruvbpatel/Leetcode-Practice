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
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        // map ->vertical->level->values
        map<int,map<int,multiset<int>>> nodes; 
        
        queue<pair<TreeNode*,pair<int,int>>> q;
        
        q.push({root,{0,0}});  /// {node,{vertical,level}};
            
        while(!q.empty()){
            
            auto p = q.front();
            q.pop();
            
            TreeNode* currnode = p.first;
            int vertical = p.second.first;
            int level = p.second.second;
            
            nodes[vertical][level].insert(currnode->val);
            
            if(currnode->left){
                q.push({currnode->left,{vertical-1,level+1}});
            }
            
            if(currnode->right){
                q.push({currnode->right,{vertical+1,level+1}});
            }
            
        }
        
        vector<vector<int>> ans;
        
        for(auto p:nodes){
            
            vector<int> col; 
            
            for(auto q:p.second){// iterate over multiset;
                col.insert(col.end(),q.second.begin(),q.second.end()); // insrt at end of col
            }
            ans.push_back(col);
        }
        
        return ans;
    }
};