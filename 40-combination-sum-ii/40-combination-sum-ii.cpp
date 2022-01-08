class Solution {
public:
    
    void solve(vector<int>& arr,int idx,int target,vector<int>& temp,vector<vector<int>>& ans){
        
        
        if(target==0){
            ans.push_back(temp);
            return;
        }
           
        
        for(int i=idx;i<arr.size();i++){
            
            if(arr[idx]>target) break; // if curr ele is bigger than target then all rest wil be bigger so no point in includingh
            
            if(i>idx and arr[i]==arr[i-1])
                continue;  // skip taking duplicate elements;
            
            // if not duplicate then include and try
            temp.push_back(arr[i]);
            solve(arr,i+1,target-arr[i],temp,ans);
            temp.pop_back();
        }
        
        
        
    }
    
    
    vector<vector<int>> combinationSum2(vector<int>& arr, int target) {
        
        sort(arr.begin(),arr.end());
        
        
        vector<vector<int>> ans;
        
        vector<int> temp;
        
        solve(arr,0,target,temp,ans);
                
        return ans;
        
    }
};