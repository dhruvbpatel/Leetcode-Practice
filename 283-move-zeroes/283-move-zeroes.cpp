class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        
        int lastOccur = 0;
        
        for(int curr= 0;curr<nums.size();curr++){
            if(nums[curr]!=0){
                swap(nums[lastOccur++],nums[curr]);
            }
        }
        
        
    }
};