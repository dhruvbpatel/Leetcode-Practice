class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        int ans = 0;
        int leftmin = prices[0];
        
        
        for(int i = 1;i<prices.size();i++){
            
            if(prices[i]<leftmin) leftmin = prices[i];
            else
                ans = max(prices[i]-leftmin,ans);
            
        }
        
        return ans;
        
    }
};