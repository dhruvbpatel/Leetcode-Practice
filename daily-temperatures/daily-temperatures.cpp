class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& arr) {
        
        stack<int> st;
        
        int n = arr.size();
        
        vector<int> ans(n,0);
        
        for(int i=0;i<n;i++){
            
            int curr = arr[i];
            
            while(!st.empty() and arr[st.top()]<curr){
                
                int prev = st.top();
                st.pop();
                ans[prev] = i-prev;
                
            }
            
            st.push(i);
            
            
            
        }
        
        
        return ans;
        
        
    }
};