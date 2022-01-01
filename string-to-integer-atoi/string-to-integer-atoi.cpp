class Solution {
public:
    int myAtoi(string s) {
        
        
        long index = s.find_first_not_of(' '); // trim space
        
        if(index == string::npos){
            return 0;
        }
        
        
            
        
        long ans = 0;
        
        bool neg = false;
        
         if(s[index]=='-'){
                neg = true;
                index++;
        }
        
        else if(s[index]=='+'){
            index++;
        }
        
        
        
        for(int i = index;i<s.length();i++){
           
            if(isdigit(s[i])){
                
                ans = ans*10 + (s[i]-'0');
                
                if(neg && -ans<=INT_MIN) return INT_MIN;
                if(!neg && ans>=INT_MAX) return INT_MAX;
                
            }else{
                break;
            }
            
            
        }
        
        if(neg){
            ans = -ans;
        }
        
        
        return int(ans);
    }
};