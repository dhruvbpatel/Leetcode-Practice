class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        def add(l,r):
            
            if l==r:
                return str(l)
            
            return str(l)+"->"+str(r)
        
        
        ans = []
        prev = lower-1
        
        for i in range(len(nums)+1):
            
            curr = nums[i] if i<len(nums) else upper+1
            
            if prev+1<=curr-1:
                ans.append(add(prev+1,curr-1))
            
            prev = curr
        
        return ans
        
        