class Solution {
public:
    
    class Comp{
        public:
        
        bool operator()( pair<int,string>& a,  pair<int,string>& b){
            if(a.first==b.first) return a.second<b.second;
            
            return a.first>b.first;
        }
    };
    
    
    vector<string> topKFrequent(vector<string>& words, int k) {
        
        int n = words.size();
        
        if(n==k){
            sort(words.begin(),words.end());
            return words;
        }
        
        
        unordered_map<string,int> mp;
        
        
        for(auto i:words){
            mp[i]++;
        }
        
        priority_queue<pair<int,string>, vector<pair<int,string>>,Comp> pq;
        // created a min heap by custom comparator;
        
        for(auto it:mp){
            
            pq.push({it.second,it.first});
            
            
            if(pq.size()>k){
                pq.pop();
            }
        }
        
        
        vector<string> ans(k);
        
        int m = k-1;
        
        while(pq.size()>0){
            ans[m--] = pq.top().second;
            // cout<<pq.top().second<<endl;
            pq.pop();
        }
        
        return ans;
        
        
    }
};