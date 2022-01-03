class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        
        unordered_map<int,int> mp;
        
        for(auto i:nums){
            mp[i]++;
        }
        
        
        int count = 0;
        
        
        for(auto it=mp.begin();it!=mp.end();it++){
            
            if(k>0 ){
                
                if(mp.find(it->first+k)!=mp.end()){
                    count++;
                }
                // count++;
            }
            
            else if(k==0 and mp[it->first]>1)
                count++;
        }
        
        return count;
        
        
    }
};