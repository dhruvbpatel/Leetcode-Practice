class Solution:
    
    def solve(self,ip,op,ans,idx):
        
        if(len(ip)==idx):
            ans.append(op)
            return
        
        op1 = list()
        op1.extend(op)
        op1.append(ip[idx])
        
        self.solve(ip,op1,ans,idx+1)
        self.solve(ip,op,ans,idx+1)
        
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        op =list()
        idx =0
        
        self.solve(nums,op,ans,idx);
        return ans
        