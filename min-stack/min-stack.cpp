class MinStack {
public:
    
    stack<int> st;
    stack<int> minSt;
    int mn = INT_MAX;
    
    
    MinStack() {
        
    }
    
    void push(int val) {
        
        if(st.empty()){
            st.push(val);
            minSt.push(val);
            
        }else{
            
            st.push(val);
          
            if(val>minSt.top()){
                minSt.push(minSt.top());
                
            }else{
                minSt.push(val);
            }
            
        }
        
    }
    
    void pop() {
        
        st.pop();
        minSt.pop();
        
    }
    
    int top() {
        int val = st.top();
        return val;
    }
    
    int getMin() {
        int val = minSt.top();
        return val;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */