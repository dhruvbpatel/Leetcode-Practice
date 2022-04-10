class Solution {
public:
    int calPoints(vector<string>& ops) {
        
        stack<int> st;
        
        for(auto it:ops){
            
            if(it=="+"){
                
                int first = st.top();
                st.pop();
                int newtop = st.top()+first;
                st.push(first);
                st.push(newtop);
                
            }else if(it=="C"){
                st.pop();
                
            }else if(it=="D"){
                st.push(2*st.top());
                
            }else{
                st.push(stoi(it));
            }
        }
        
        int sum =0;
        
        while(st.size()!=0){
            sum+=st.top();
            st.pop();
        }
        
        return sum;
        
    }
};