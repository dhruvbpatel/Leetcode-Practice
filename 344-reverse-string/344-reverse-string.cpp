class Solution {
public:
    
    void helper(int start,int end, vector<char>& s){
        
        if(start>=end){
            return;
        }
        
        swap(s[start],s[end]);
        
        helper(start+1,end-1,s);
        
    }
    
    void reverseString(vector<char>& s) {
        
        helper(0,s.size()-1,s);              
        
        
    }
};