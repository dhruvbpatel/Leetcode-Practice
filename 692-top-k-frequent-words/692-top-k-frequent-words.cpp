class Solution {
public:
    
    class Comp{
        public:
        
        bool operator()( pair<int,string>& a,  pair<int,string>& b){
            
            // for max heap : max at top
            // if(a.first==b.first) return a.second>b.second; 
            // return a.first<b.first; // descending order to be stores in pq
            // order:
            // i 2
            // love 2
            // coding 1
            // leetcode 1
                     
            
            // min heap -> final 
            if(a.first==b.first) return a.second<b.second; // in lexigraphic order smaller first
            return a.first>b.first; // descending order to be stores in pq ; greater first
            
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
        
        priority_queue<pair<int,string>, vector<pair<int,string>>,Comp> pq; // max heap
        // created a custom heap by custom comparator;
        
        
        
        for(auto it:mp){
            
            pq.push({it.second,it.first}); // here we push all elements in array
            
            // we use min heap so pop min elements with min freq if size exceeds
            if(pq.size()>k){
                pq.pop();
            }
            
        }
        
        // while(!pq.empty()){
        //     cout<<pq.top().second<<" "<<pq.top().first<<endl;
        //     pq.pop();
        // }
        
        vector<string> ans(k);
        
        int m = k-1;
        
        // int m= 0;
        
        while(!pq.empty()){
            ans[m--] = pq.top().second;
            // ans[m++] = pq.top().second;
            // cout<<pq.top().second<<endl;
            pq.pop();
        }
        
        return ans;
        
        
    }
};