class Solution:
    
    def solve(self,idx,nums,temp,ans):
    
        if(idx==len(nums)):
            ans.append(list(nums))
            return
        
        for i in range(idx,len(nums)):
            nums[i],nums[idx] = nums[idx],nums[i]
            self.solve(idx+1,nums,temp,ans);
            nums[i],nums[idx] = nums[idx],nums[i]
            
        
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        idx = 0
        ans = []
        temp = []
        self.solve(idx,nums,temp,ans)
        
        return ans