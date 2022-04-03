class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        
        if(nums.size()==0){
            return;
        }
        
        int n = nums.size();
        int k, l;
        // k ->breakpoint
        // l = idx2
        
        for(k=n-2;k>=0;k--){  // we first find the breakpoint where it is less than i+1;
            if(nums[k]<nums[k+1]){
                break; // if we find we break 
            }
        }
        
        if(k<0){  // if breakpoint is -ve then we didn;t find anything in array i.e our array is at last permute , so reverse 
            reverse(nums.begin(),nums.end());
            return;
        }
        else{ // if we found k
            
            for(l = n-1;l>k;l--){
                if(nums[l]>nums[k]){  // now we found a idx which is greater than breakpoint as it will be our next element in permute
                    break;
                }
            }
            
        }
        
        swap(nums[l],nums[k]); // swap both idx
        reverse(nums.begin()+k+1,nums.end()); // now reverse others
        
        
    }
};