class Solution {
public:
    
    
    int getLCS(string s1,string s2,int n,int m){

        if(n==0 or m==0){
            return 0;
        }

        if(s1[n-1]==s2[m-1]){
            return 1+getLCS(s1,s2,n-1,m-1);
        }
        // else
        return max(getLCS(s1,s2,n,m-1),getLCS(s1,s2,n-1,m));



    }
    
    
int getLCSMemoized(string s1,string s2, int n, int m,vector<vector<int>>& dp){

    if(n==0 or m==0){
        return 0;
    }

    if(dp[n][m]!=-1){
        return dp[n][m];
    }

    if(s1[n-1]==s2[m-1]){
        return dp[n][m] = 1+getLCSMemoized(s1,s2,n-1,m-1,dp);
    }

    return dp[n][m] = max(
        getLCSMemoized(s1,s2,n,m-1,dp),getLCSMemoized(s1,s2,n-1,m,dp)
    );
    
}
    
    int getLCSdp(string s1,string s2,int n,int m){
        
        vector<vector<int>> dp(n+1,vector<int>(m+1));
        
        for(int i=0;i<n+1;i++){
            for(int j=0;j<m+1;j++){
                if(i==0 or j==0) dp[i][j]=0;
            }
        }
        
        // dp[0][0] = 0;
        
        for(int i=1;i<n+1;i++){
            for(int j=1;j<m+1;j++){
                
                if(s1[i-1]==s2[j-1]){
                    dp[i][j] = 1+ dp[i-1][j-1];
                }else{
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j]);
                }
                
            }
        }
        
        return dp[n][m];
    }


    
    int longestCommonSubsequence(string s1, string s2) {
        
        int n = s1.length();
        int m = s2.length();
        
        
        // vector<vector<int>> dp(n+1,vector<int>(m+1,-1));

        
        // return getLCS(s1,s2,n,m);
        // return getLCSMemoized(s1,s2,n,m,dp);
        return getLCSdp(s1,s2,n,m);
        
    }
};