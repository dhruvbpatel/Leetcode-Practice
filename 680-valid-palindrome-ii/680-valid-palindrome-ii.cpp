class Solution {
public:
    
    bool checkPalindrome(string s,int l,int r){
        while(l<=r){
            if(s[l++]!=s[r--]) return false;
        }
        
        return true;
    }
    
    bool validPalindrome(string s) {
        
        int l = 0;
        int r = s.size()-1;
        
        while(l<=r){
            if(s[l]!=s[r]){
                return (checkPalindrome(s,l+1,r) or checkPalindrome(s,l,r-1));
            }
            
            l++;
            r--;
        }
        return true;
    }
};