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
                
                // if curr element is max of all left side so no water will be stored here
                 // as no left boundary exists for curr element
                
                else{
                    
                    
                    /*
                    
                    how can we say that we have the ans:
                   1)  because here our curr arr[l] is not maximum if it was then we wont be in this else
                    thus we gaurntee that we have a left wall greater than curr, i.e leftmaxl
                    
                    2) now for right boundary we are coming to this position only after we hve 
                    checked that arr[l]<=arr[r]
                    thus there is atleast one element that is greater than equal curr so right boundary 
                    exists
                    
                    
                    */
                    
                    ans+= leftmax - arr[l]; 
                    
                    
                    
                }
                
                l++;
                
            }else{
                // when arr[r]<arr[l];
                
                if(arr[r]>=rightmax){
                    
                    rightmax = arr[r];  // same intuition for right side 
                    // if right max is smaller then there is not bigger right wall for current element
                    // so water cant be stored here
                    
                }else{
                    ans+= rightmax-arr[r];
                    
                    // if we reach in this else mens our left pointer is greater than right and
                    // right is also not right max so we have both walls
                    // so we will be having water stored here;
                    
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