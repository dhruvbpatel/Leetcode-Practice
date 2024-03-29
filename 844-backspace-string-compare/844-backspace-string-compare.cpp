class Solution {
public:
    bool backspaceCompare(string s, string t) {
        
        int k=0; // k is pointer of s
        
        int p = 0; // p is pointer for t
        
        // here we modify strings , remove # and back character and compare at the end
        
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='#')
            {
                k--; // 
                 k=max(0,k);
            }
            
           else
           {
               s[k]=s[i];
               k++;
           }
        }
        for(int i=0;i<t.size();i++)
        {
            if(t[i]=='#')
            {
                p--;
                 p=max(0,p);
            }
            
           else
           {
               t[p]=t[i];
               p++;
           }
        }
        if(k!=p)
            return false;
        else
        {
            for(int i=0;i<k;i++)
            {
                if(s[i]!=t[i])
                    return false;
            }
            return true;
        }
        
    
    }
};