class Solution {
public:
    
    
    int change(int amount, vector<int>& coins) {
        
        int n = coins.size();
        
        if(n==1){
            if(amount==coins[0]){
                return 1;
            }
            if(amount%coins[0]==0){
                return 1;
            }else{
                return 0;
            }
        }
        
        vector<vector<int>> dp(n+1,vector<int>(amount+1));
        
        for(int i=0;i<n+1;i++){
            for(int j=0;j<amount+1;j++){
                if(j==0) dp[i][j]=1;
                if(i==0) dp[i][j]=0;
            }
        }
        
        
        dp[0][0] = 0;
        
        
        for(int i=1;i<n+1;i++){
            for(int j=1;j<amount+1;j++){
                
                if(coins[i-1]<=j){
                    dp[i][j] = dp[i][j-coins[i-1]] + dp[i-1][j];
                }else{
                    dp[i][j] = dp[i-1][j];
                }
                
            }
        }
        
        return dp[n][amount];
        
    }
};