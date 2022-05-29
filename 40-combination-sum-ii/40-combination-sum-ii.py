class Solution:
    
    def solve(self,idx,target,nums,temp,ans):
        
        if(target==0):
            ans.append(list(temp))
        
        for i in range(idx,len(nums)):
            
            if(nums[i]>target):
                break
            
            if(idx!=i and nums[i]==nums[i-1]):
                continue
            
            temp.append(nums[i])
            self.solve(i+1,target-nums[i],nums,temp,ans)
            temp.pop()
            
        
        
        
    
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        idx = 0
        temp = []
        ans = []
        nums.sort()
        
        self.solve(idx,target,nums,temp,ans)
        return ans
        