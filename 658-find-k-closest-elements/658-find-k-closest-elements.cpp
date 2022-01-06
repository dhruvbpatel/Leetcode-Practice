class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        
        priority_queue<pair<int,int>> pq; // max heap
        // stores abs(diff), arr[i];
        
        int n = arr.size();
        vector<int> ans;
        
        
        for(int i=0;i<n;i++){
            int diff = abs(arr[i]-x);
            
            pq.push({diff,arr[i]});
            
            if(pq.size()>k){
                pq.pop();
            }
        }
        
        while(!pq.empty()){
            int val = pq.top().second;
            ans.push_back(val);
            pq.pop();
        }
        
        sort(ans.begin(),ans.end());
        return ans;
    }
};