class Solution {
public:
    string longestPalindrome(string s) {
        
        int n  = s.size();
        
        vector<vector<int>> dp(n,vector<int>(n,0));
        
        int start=0 ,len=0;
        
        for(int k=0;k<n;k++){ // for length of string of size 0,1...2..3...etc till n
            for(int i=0,j=k;j<n;j++,i++){ // iterate over dp 
                if(k==0) dp[i][j]=1;
                else if(k==1) dp[i][j] = s[i]==s[j];
                else dp[i][j] = s[i]==s[j] && dp[i+1][j-1];
                
                if(dp[i][j]){
                    len = k;
                    start=i;
                }
            }
        }
        
        
        return s.substr(start,len+1); // last index is not included so +1
        
        
        
    }
};