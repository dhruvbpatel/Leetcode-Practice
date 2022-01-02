class Solution {
public:
    
    class Comp{
        public:
        
        bool operator()(pair<int,int>& a,pair<int,int>& b){
           return a.second<b.second;
        }
            
    };
    
    vector<int> topKFrequent(vector<int>& nums, int k) {
        
        if(k==nums.size()){
            return nums;
        }
        
        
        vector<int> ans;
        
        unordered_map<int,int> mp;
        
        for(auto i:nums){
            mp[i]++;
        }
        // int,freq
        
        priority_queue<pair<int,int>,vector<pair<int,int>>,Comp> pq;
        
        for(auto it:mp){
            pq.push({it.first,it.second});
            
//             if(pq.size()>k){
//                 pq.pop();
//             }
                
        }
        
        while(k--){
            ans.push_back(pq.top().first);
            pq.pop();
        }
        
        return ans;
        
        
        
        
        
        
        
        
        
        
    }
};