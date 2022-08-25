class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
              
        
        ans = sys.maxsize
        l = 0
        total = 0
        
        for r in range(len(nums)):
            total+=nums[r] #subarray l-r sum
            
            while(total>=target): #current subarray sum is greater or equal try for smaller
                ans = min(ans,r-l+1) #current length and update if min
                total-=nums[l] #remove left sum
                l+=1 # increment left pointer
            
        return ans if ans is not sys.maxsize else 0
        
        #time: O(n) #inner loop runs for 1 time in avg case till smaller sum is obtained
        
        