class Solution {
public:
    int trap(vector<int>& arr) {
        
        // 2 pointer approach;
        
        int leftmax = 0;
        int rightmax = 0;
        
        int l = 0;
        int r = arr.size()-1;
        
        int ans = 0;
        
        
        while(l<=r){
            
            if(arr[l]<=arr[r]){
                
                if(arr[l]>=leftmax) leftmax = arr[l];
                
                else{
                    ans+= leftmax - arr[l];
                }
                
                l++;
                
            }else{
                // when arr[r]<arr[l];
                
                if(arr[r]>=rightmax){
                    rightmax = arr[r];
                }else{
                    ans+= rightmax-arr[r];
                }
                
                r--;
            }
            
        }
        
        return ans;
        
        
        
        
        
        // stack approach;
//         stack<int> st;
        
//         int n = arr.size();
        
//         int ans = 0;
        
//         for(int i=0;i<n;i++){
            
//             while(!st.empty() and arr[st.top()]<arr[i]){  // if we found curr element is greatert than top of stack do while it is not
                
//                 int curr = st.top(); // top index
//                 st.pop();
                
//                 if(st.empty()){
//                     break; // this handles if there is not left boundary i.e bigger element is at 1th index
//                 }
                
//                 int diff = i-st.top()-1; // length difference 
//                 // subtract curr because current element height will be not storing water 
//                 ans+= (min(arr[st.top()],arr[i])-arr[curr])*diff;
                            
                
//             }
            
//             // if not greater than top 
//             st.push(i);
            
//         }
        
//         return ans;
    }
};