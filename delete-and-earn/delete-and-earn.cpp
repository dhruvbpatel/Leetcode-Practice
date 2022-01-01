class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        
        int n = nums.size();
        if(n==1) return nums[0];
        
        
        n = *max_element(nums.begin(),nums.end());
        
        vector<int> count(n+1,0);
        
        for(auto i:nums) count[i]+=i; // stores index with total count
        
        
        
        vector<int> dp(n+1,0); // dp[i] repesents number with i value
        
        dp[0] = 0; // if we take 0 we earn 0
        dp[1] = count[1]; // we take 1 then we earn count of 1 in array
        
        for(int i=2;i<count.size();i++){
            
            dp[i] = max(dp[i-1],dp[i-2]+count[i]);
            
        }
        
        return dp[n];
        
        
        
        
    }
};