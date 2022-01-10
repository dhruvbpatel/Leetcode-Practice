class Solution {
public:
    int search(vector<int>& arr, int target) {
        
        int low = 0;
        int high  = arr.size()-1;
        int mid;
        
        while(low<=high){
            
            int mid = (low+ (high-low)/2);
            
            if(arr[mid]==target) return mid;
            
            
            // if left side is sorted
            if(arr[low]<=arr[mid]){
                
                if(target>=arr[low] and target<=arr[mid]){  // check if target is in left half
                    high = mid-1;
                }else{
                    low = mid + 1;
                }
                
            }else{
                // righht side sorted;
                
                if(target>=arr[mid] and target<=arr[high]){ //  check if it is in right half
                    low =mid+1;
                }else{
                    high = mid-1;
                }
                
            }
            
        }
        
        return -1;
        
    }
};