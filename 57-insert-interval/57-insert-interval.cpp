class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        
        vector<vector<int>> ans;
        
        
        vector<int> temp = newInterval;
        
        for(auto it:intervals){
            
            if(it[0]<=temp[1] and it[1]>=temp[0]){
                temp[0] = min(it[0],temp[0]);
                temp[1] = max(it[1],temp[1]);
                
            } else if(temp[1]<it[0]){
              ans.push_back(temp);
               temp = it; 
            } else{
                ans.push_back(it);
                
            }
            
        }
        
        ans.push_back(temp);
        
        
        return ans;
        
        
        
        
        
    }
};