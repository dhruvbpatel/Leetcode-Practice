class Solution {
public:
    
    int dp[2001][2001];
    
    bool isPalindrome(string& s,int i,int j){
        
        while(i<=j){
            if(s[i++]!=s[j--]) return false;
        }
        return true;
        
    }
    
    int solve(string& s,int i,int j){
        
        
        if(i>=j) return 0;
        
        if(isPalindrome(s,i,j)==true){
            dp[i][j] = 0;
            return 0;
        }
        
        if(dp[i][j]!=-1) return dp[i][j];
        
        int mn = INT_MAX;
        int left,right;
        for(int k=i;k<=j-1;k++){
            
            if(isPalindrome(s,i,k)){
                
           if(dp[i][k]!=-1){
                left=dp[i][k];
            }
            else{
                left=solve(s,i,k);
                dp[i][k]=left;
            }
            if(dp[k+1][j]!=-1){
                right=dp[k+1][j];
            }
            else{
                right=solve(s,k+1,j);
                dp[k+1][j]=right;
            }
            int temp=1+left+right;
            mn=min(temp,mn);
            }
            
//             int left,right;
            
//             if(dp[i][k]!=-1){
//                 left = dp[i][k];
//             }else{
//                 left = solve(s,i,k);
//                 dp[i][k] = left;
//             }
            
//             if(dp[k+1][j]!=-1){
//                 right = dp[k+1][j];
//                 dp[k+1][j] = right;
//             }
//             else{
//                 right = solve(s,k+1,j);
//             }
            
//             // int temp = 1 + solve(s,i,k,dp) + solve(s,k+1,j,dp);
//             int temp = 1+left+right;
//             mn =min(mn,temp);
            
        }
        
        return dp[i][j] =  mn;
        
    }
    
    int minCut(string s) {
       
        int n = s.size();
        
        if(isPalindrome(s,0,n-1)) return 0;
        
        memset(dp,-1, sizeof(dp));


        return solve(s,0,n-1);
        
        
    }
};