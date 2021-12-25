class Solution {
public:
        
    void solve(int open,int close,string op, vector<string>& ans){
        
        if(open==0 and close==0){
            ans.push_back(op);
            return;
        }
        
        if(open!=0){  // if open is not zero we can append open 
            
            string op1 = op;
            op1.push_back('(');
            
            solve(open-1,close,op1,ans);
            
        }
        
        if(close>open){  //if open is less than close
            string op2 = op;
            op2.push_back(')');
            
            solve(open,close-1,op2,ans);
            return;
        }
        
        
    }
    
    // make recursive tree 
    vector<string> generateParenthesis(int n) {
        
        vector<string> ans;
        
        int open = n;
        int close = n;
        
        string op = "";
        
        solve(open,close,op,ans);
        
        return ans;
        
        
        
    }
};