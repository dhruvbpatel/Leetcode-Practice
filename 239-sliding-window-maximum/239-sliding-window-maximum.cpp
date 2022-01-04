class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        
        vector<int> ans;
        deque<int> dq;
        
        for(int i=0;i<nums.size();i++){
            
            if(!dq.empty() and dq.front()== (i-k)){ // check for out of bound index for size k subarray
                dq.pop_front();
            }
            
//             if we encounter a large number our decreasing deque will be breaked so we will pop until our 
//                 current element is greater than element at back of deque or dq empty
            while(!dq.empty() and nums[dq.back()]<nums[i]){ 
                dq.pop_back();
            }
            
            dq.push_back(i);  // now add current index
            
            //
            if(i>=k-1){  // only if k elements are iterated 1st then start pushing in ans;
                // because until we iterate over k elements we will not add to ans;
                ans.push_back(nums[dq.front()]); 
            }
        }
        
        return ans;
    }
};