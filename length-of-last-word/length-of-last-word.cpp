class Solution {
public:
    int lengthOfLastWord(string s) {
        
        string ans ="";
        
        int n = s.length();
        int i =n-1;
        
        if(s[i]==' ' and i!=0){
            while(s[i]==' ' and  i!=0){
                i--;
            } 
            
        }
        
        while(s[i]!=' ' and i!=0){
            ans+=s[i];
            i--;
            
            
        }
        
        if(i==0 and s[i]!=' ') ans+=s[i];
        
        
        return ans.length();
        
        
        
    }
};