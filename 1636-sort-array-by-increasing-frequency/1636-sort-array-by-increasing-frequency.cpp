class Solution {
public:
    typedef pair<int,int> p;
    
    class compare
    {
        public:
        bool operator()(p x,p y)
        {   
            if(x.first==y.first)
            {
                return x.second<y.second; // if equal then in decreasing 
            }
            return (x.first>y.first); // first sort by no frequency in increasing order
        }
    };
    
    vector<int> frequencySort(vector<int>& nums) {
        
        unordered_map<int,int> mp;
        
        for(auto it:nums){
            mp[it]+=1;
        }
        
        vector<int> ans;
        priority_queue<p,vector<p>,compare> pq; // min heap;
        
        for(auto it=mp.begin();it!=mp.end();it++){
            
            pq.push({it->second,it->first});
        }
        
        while(!pq.empty()){
           
            int curr = pq.top().first;
            
            while(curr--){
                ans.push_back(pq.top().second);
            }
            
            pq.pop();
            
        }
        
        
        return ans;
        
    }
};