class Solution {
public:
    
    
    int rob(vector<int>& nums) {
        
        
        // we have to take 2 case
        // 1st when we will rob 1st house then we can't rob last house
        // 2nd when we will not rob 1st house the we will rob  2nd and last house;
        
        
        // we will take 2 seperate vector for both case and it's same as house robber
        
        int n = nums.size();
        
        if(n==1) return nums[0];
        if(n==2) return max(nums[0],nums[1]);
        
        vector<int> dp1(n);
        vector<int> dp2(n);
        
        
        // we rob 1st house;
        
        dp1[0] = nums[0];
        dp1[1] = nums[0]; // we can't rob 2nd house in this case;
        
        
        // we dont rob 1st house;
        dp2[0] = 0;
        dp2[1] = nums[1];
        
        // apply house robber approach
        
        for(int i=2;i<n;i++){
            dp1[i] = max(nums[i] + dp1[i-2], dp1[i-1]);
            dp2[i] = max(nums[i] + dp2[i-2], dp2[i-1]);
        }
        
        // now dp1 is till n-2 as we rob 1st house so we need to ignore last house
        // dp2 is till last house n-1;
        
        return max(dp1[n-2], dp2[n-1]);
        
      
        
        
        
    }
};