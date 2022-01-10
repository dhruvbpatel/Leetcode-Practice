class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& arr) {
        
        
        vector<vector<int>> ans;
        
        if(arr.size()==0){
            return ans;
        }
        
        sort(arr.begin(),arr.end());
        
        vector<int> temp = arr[0];
        
        for(auto it:arr){
            if(it[0]<=temp[1]){
                temp[1] = max(it[1],temp[1]);
            }else{
                ans.push_back(temp);
                temp = it;
            }
        }
        
        ans.push_back(temp);
        return ans;
        
        
        
        
        
        
        
    }
};