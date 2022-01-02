class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        
        int n = nums.size();
        
        if(n==0 or n==1) return n;
        
        
        unordered_map<int,int> mp;
        
        for(auto i:nums){
            mp[i]++;
        }
        
        int ans = 0;
        
        for(int i=0;i<nums.size();i++){
            
            if(mp[nums[i]-1]){
                continue;
            }else{
                int count = 0;
                int val = nums[i];
                while(mp[val]!=0){
                    count++;
                    val++;
                }
                ans  = max(count,ans);
            }
            
        }
        
        return ans;
        
    }
};