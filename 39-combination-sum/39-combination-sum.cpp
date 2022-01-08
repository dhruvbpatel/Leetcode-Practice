class Solution {
public:
    
    
    void solve(vector<int>& arr,int idx,int target,vector<vector<int>>& ans,vector<int>& temp){
        
        if(idx==arr.size()){
            if(target==0){
                ans.push_back(temp);
                
            }
            return;
        }
        
        
        // int curr = arr[idx];
        
        if(arr[idx]<=target){ // if curr element is less than target
            
            temp.push_back(arr[idx]); // push in temp
            // target = target-arr[idx];
            solve(arr,idx,target-arr[idx],ans,temp); // decrease target and dont increase idx as we can reuse
            temp.pop_back(); 
            
        }
        // idx+=1;
        solve(arr,idx+1,target,ans,temp);
        
        
        
        
        
    }
    
    
    
    vector<vector<int>> combinationSum(vector<int>& arr, int target) {
        
        vector<vector<int>> ans;
        
        vector<int> temp;
        
        solve(arr,0,target,ans,temp);
        return ans;
    }
};