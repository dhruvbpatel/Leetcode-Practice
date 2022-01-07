class Solution {
public:
    typedef pair<int,int> pi;
    
    vector<int> topKFrequent(vector<int>& nums, int k) {
        
        unordered_map<int,int> mp;
        
        int n = nums.size();
        if(k==n) return nums;
        
        vector<int> ans;
        
        for(auto it:nums)
            mp[it]+=1;
        
        priority_queue<pi,vector<pi>,greater<pi>> pq; // min heap
        
        for(auto it=mp.begin();it!=mp.end();it++){
            
            pq.push({it->second,it->first});
            
            if(pq.size()>k){
                pq.pop();
            }
        }
        
        while(!pq.empty()){
            ans.push_back(pq.top().second);
            pq.pop();
        }
        
        return ans;
        
        
    }
};