class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        ans = 0
        
        for c in range(len(strs[0])):
            for r in range(1,len(strs)):
                
                if strs[r][c]<strs[r-1][c]:
                    ans+=1
                    break
        return ans
            
        