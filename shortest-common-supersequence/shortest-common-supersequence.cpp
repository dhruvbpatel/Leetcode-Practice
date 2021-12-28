class Solution {
public:
    string shortestCommonSupersequence(string s1, string s2) {
        
        
        int n = s1.length();
        int m = s2.length();
        
        vector<vector<int>> dp(n+1,vector<int>(m+1,0));
        
        // get lcs
        for(int i=1;i<n+1;i++){
            for(int j=1;j<m+1;j++){
                
                if(s1[i-1]==s2[j-1]){
                    dp[i][j] = dp[i-1][j-1]+ 1;
                }else{
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1]);
                }
                
            }
        }
        
        int i =n;
        int j = m;
        
        string ans ="";
        
        while(i>0 and j>0){
            
            if(s1[i-1]==s2[j-1]){
                ans+=s1[i-1];
                i--;
                j--;
            }else{
                
                if(dp[i][j-1]>dp[i-1][j]){
                    ans+=s2[j-1];  // j string is b and we change j here
                    j--;
                }else{
                    ans+=s1[i-1];
                    i--;
                }
                
                
            }
            
        }
        
        while(i>0){
            ans+=s1[i-1];
            i--;
        }
        
        while(j>0){
            ans+=s2[j-1];
            j--;
        }
        
        reverse(ans.begin(),ans.end());
        
        return ans;
        
        
        
    }
};