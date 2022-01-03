class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& arr) {
        
        vector<int> start;
        vector<int> end;
        
        int n = arr.size();
        
        for(int i=0;i<n;i++){
            start.push_back(arr[i][0]);
            end.push_back(arr[i][1]);
        }
        
        sort(start.begin(),start.end());
        sort(end.begin(),end.end());
        
        int i=0; // start pointer
        int j =0; // end pointer
        
         int count = 0;
        int ans = 0;
        
        while(i<n){
            
            if(start[i]<end[j]){
                i++;
                count++;
                
            }else{  // if start >=end ; 
                
                // if end==star also we need to increment j pointer and decrement count
                
                j++;
                count--;
                
            }
            
            ans = max(count,ans);
            
            
        }
        return ans;
        
    }
};