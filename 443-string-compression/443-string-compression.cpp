class Solution {
public:
    int compress(vector<char>& chars) {
     
        if(chars.size()==1){
            return 1;
        }
        
        int slow=0;
        int fast=0;
        
        while(fast<chars.size()){
            chars[slow] = chars[fast];
            int count = 0;
            
            while(fast<chars.size() and chars[fast]==chars[slow]){
                fast++;
                count++;
            }
            
            if(count==1){
                slow++; // count is one , move ahead slow pointer
            }else{
                string curr_count = to_string(count);
                for(auto c:curr_count){
                    // slow+=1; // increment slow
                    chars[++slow]=c; // update slow pos
                } 
                slow++;// move ahead slow
            }
            
            
            
                
                
        }
        
        return slow;
        
        
        
    }
};