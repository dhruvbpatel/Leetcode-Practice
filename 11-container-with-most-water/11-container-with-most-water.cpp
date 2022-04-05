class Solution {
public:
    int maxArea(vector<int>& arr) {
        
        int l = 0;
        int r  = arr.size()-1;
        int ans=0;
        while(l<r){
            
            ans = max(ans,min(arr[l],arr[r])*(r-l));
            
            if(arr[l]<arr[r]){
                l++;
            }else{
                r--;
            }
            
            
        }
        
        return ans;
        
    }
};