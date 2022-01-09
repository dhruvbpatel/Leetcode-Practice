class Solution {
public:
    
    int getTwoSumSmaller(vector<int>& nums,int start,int target){
        
        int sum = 0;
        int l = start;
        int r = nums.size()-1;
        
        while(l<r){
            if(nums[l]+nums[r]<target){
                sum+=(r-l);
                l++;
            }else{
                r--;
            }
        }
        return sum;
        
    }
    
    int threeSumSmaller(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        if(nums.size()<3){
            return 0;
        }
        
        int sum = 0;
        
        for(int i=0;i<nums.size()-2;i++){
            sum+= getTwoSumSmaller(nums,i+1,target-nums[i]);
        }
        return sum;
    }
    
};