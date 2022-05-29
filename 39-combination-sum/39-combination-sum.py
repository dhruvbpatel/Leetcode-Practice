class Solution:
    
    def solve(self,idx,target,nums,temp,ans):
        
        if(idx==len(nums)):
            if(target==0):
                ans.append(list(temp));
            
            return
        
        if(nums[idx]<=target):
            
            temp.append(nums[idx])
            self.solve(idx,target-nums[idx],nums,temp,ans)
            temp.pop()
        
        self.solve(idx+1,target,nums,temp,ans);
            
            
    
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        idx = 0
        temp = []
        ans = []
        
        self.solve(idx,target,nums,temp,ans);
        return ans
        
        