class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        curr = 0
        mx = 0
        
        for n in nums:
            if n==1:
                curr+=1
            else:
                mx = max(mx,curr)
                curr=0
        
        return max(curr,mx)