class Solution:
    
    def solve(self,idx,ip,op,ans):
        
        ans.append(list(op))  ## what we do in 1st step is add op in ans, it can be empty for 1st iterations
        
        for i in range(idx,len(ip)): # now iterate from idx to end of ip array
            
            if i!=idx and (ip[i]==ip[i-1]): # if it is not idx index and same value as prev index skip it,else duplicate value will be added in ans
                continue
            
            # now when we arrive at new index which is unique add it in op
            op.append(ip[i]) 
            
            self.solve(i+1,ip,op,ans); # from next index again recurse to find another pairs
            
            op.pop() # make sure to pop for considering the array in which we dont consider idx element
            
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        op = []
        ans = []
        idx = 0
        nums = sorted(nums)  ## sort the array
        
        self.solve(idx,nums,op,ans);
        return ans
        
        
        
        