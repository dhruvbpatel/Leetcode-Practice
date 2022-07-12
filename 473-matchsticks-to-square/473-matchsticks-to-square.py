class Solution:
    def _reach_target(self, matchsticks: List[int], targets: List[int]) -> bool:
        if len(targets) == 1:
            return sum(matchsticks) == targets[0]
        
        start = 0
        anchor = -1  # to make sure we can jump out same numbers in matchSticks
        while start < len(matchsticks):
            if matchsticks[start] == anchor:
                start += 1
                continue
                
            if matchsticks[start] > targets[0]:
                return False

            if matchsticks[start] == targets[0]:
                return self._reach_target(matchsticks[:start]+matchsticks[start+1:], targets[1:])

            # Condition: matchsticks[start] < targets[0]
            result = self._reach_target(matchsticks[:start]+matchsticks[start+1:], [targets[0]-matchsticks[start]]+targets[1:])
            if result:
                return True
            
			# Else we need to go on our iteration for matchSticks
            anchor = matchsticks[start]
            start += 1

        if start >= len(matchsticks):
            return False
        

    def makesquare(self, matchsticks: List[int]) -> bool:
        _sum = sum(matchsticks)
        if _sum % 4 > 0:
            return False
        length = _sum // 4
        matchsticks = sorted(matchsticks, reverse=True)
        
        return self._reach_target(matchsticks, [length]*4)
    
    
    # def makesquare(self, nums: List[int]) -> bool:
        
#         if not nums:
#             return False
        
        
#         l = len(nums)
#         perimeter = sum(nums)
        
#         #find sum
#         possible_side = perimeter//4
        
#         #cant be equally split
#         if possible_side*4!=perimeter:
#             return False
        
#         #reverse sort ,start with biggest 
#         nums.sort(reverse=True)
        
#         sums = [0 for _ in range(4)] # each 4 side
        
#         def dfs(index):
            
#             #if 3 equal side , 4th will be same so check and return true
#             if index==l:
#                 return sums[0]==sums[1]==sums[2]==possible_side
            
#             #if not equal , can belong to any of 4 side
            
#             for i in range(4):
                
#                 #if curr can fix in space left of current side
#                 if sums[i] + nums[index]<=possible_side:
                    
#                     #recurse
#                     sums[i]+=nums[index]
                    
#                     if dfs(index+1):
#                         return True
                    
#                     sums[i]-=nums[index] #backtrack
                    
#             return False # if current stick can't fit 
            
        
#         return dfs(0)
    
            