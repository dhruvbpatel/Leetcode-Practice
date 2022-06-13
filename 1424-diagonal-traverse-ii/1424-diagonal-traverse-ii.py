class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        d = collections.defaultdict(list)
        r = len(nums)
        
        for r in range(r):
            for c in range(len(nums[r])):
                d[r+c].append(nums[r][c])
                
        print(d)
        ans = []
        
        
        for k in sorted(d.keys()):
            ans.extend(d[k][::-1])
        return ans
        
        