class Solution {
public:
    string removeDuplicates(string s, int k) {
        
        stack<int> st; // to store the counter of current streak
        
        for(int i=0;i<s.size();i++){
            
            if(i==0 || s[i]!=s[i-1]){ // if differnt element push 1 in stack
                st.push(1);
            }else{
                
                if(++st.top()==k){ // increament counter as same element and if it is == k
                    st.pop(); // pop from stack
                    s.erase(i-k+1,k); // erase last k element
                    i = i-k; //. i points to just before last k elements;
                }
        
                
            }
            
            
        }
        
        return s;
        
    }
};