class Solution {
public:
    
    // unordered_map<int,int> mp;

    
    int fib(int n) {
        
        if(n==0 or n==1) return n;
              
        vector<int> dp(n);
        
        dp[0] =1;
        dp[1] =1;
        
        for(int i=2;i<n;i++)
            dp[i] = dp[i-1]+dp[i-2];
        
        return dp[n-1];
        
        
        
        
        
    }
};