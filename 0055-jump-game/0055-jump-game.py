class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        #intuition greedy:
        
        # start from back
        # from idx we can max nums[idx] steps
        # if we can reach goalpost then goalpost can be shifted to idx
        #at the end if goalpost==0 then we can reach else if goalpost >0 then its stuck
        
        
        # greedy solution 
        goalpost = len(nums)-1
        
        for idx in range(len(nums)-1,-1,-1):
            
            if idx + nums[idx] >=goalpost:
                goalpost = idx
            
        
        return True if goalpost==0 else False
    