class Solution {
public:
    
    int findBound(vector<int>& nums,int target,int lowBound){
        
        int n = nums.size();
        int l = 0;
        int r = n-1;
        
        while(l<=r){
            
            int mid =(l+r)/2;
            
            if(nums[mid]==target){
                if(lowBound==true){

                    if(mid==l or nums[mid-1]!=target){
                        return mid;
                    }

                    // when still on left side we have target element, we will find lowerbound on left side
                    r = mid-1;

                }else{

                    // we are finding upperbound

                    if(mid==r or nums[mid+1]!=target){
                        return mid;
                    }

                    l = mid+1;


                }
             }
            
          else if(nums[mid]>target){ 
              r = mid-1;
           }
            
         else{
               l = mid+1;
           }
        }
        
        return -1;
        
        
    }
    
    
    vector<int> searchRange(vector<int>& nums, int target) {
        
        int first = findBound(nums,target,true);
        
        if(first==-1) return {-1,-1};
        
        int last = findBound(nums,target,false);
        
        return {first,last};
           
    }
};