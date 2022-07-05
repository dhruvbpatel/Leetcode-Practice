class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        
        // Approach 1: Using set
        
        int n = nums.size();
        unordered_set<int> st;
        
        for(int i=0;i<n;i++){
            st.insert(nums[i]); // add in set
        }
        
        int ans = 0;
        
        for(auto n:nums){
            
            if (st.find(n-1)!=st.end()){
                continue; // not smallest
            }
            else{
                
                int count=1;
                
                while(st.find(n+count)!=st.end()){
                    count+=1;
                }
                
                ans = max(count,ans);
            }
            
        }
        
        return ans;
        
        
        // Approach:2 using map
        
//         int n = nums.size();
        
//         if(n==0 or n==1) return n;
        
        
//         unordered_map<int,int> mp;
        
//         for(auto i:nums){
//             mp[i]++;
//         }
        
//         int ans = 0;
        
//         // every time check if number smaller than curr is in mp or not
//         // if there then skip
//         // if not then we have arrived at smallest number in possible sequence
//         // then untill num++ is not in mp , increase val and check if in mp
//         // also do count ,and max cout will be ans
        
        
//         for(int i=0;i<nums.size();i++){
            
//             if(mp[nums[i]-1]){
//                 continue;
//             }else{
//                 int count = 0;
//                 int val = nums[i];
//                 while(mp[val]!=0){
//                     count++;
//                     val++;
//                 }
//                 ans  = max(count,ans);
//             }
            
//         }
        
//         return ans;
        
    }
};