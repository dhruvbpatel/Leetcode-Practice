class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        n = len(ratings)
        ans = [1]*n
        
        
        # left to right
        for i in range(n-1):
            
            if ratings[i]<ratings[i+1]:
                ans[i+1] = ans[i]+1
    
        
        #right to left
        for i in range(n-2,-1,-1):
            
            if ratings[i]>ratings[i+1]:
                ans[i] = max(ans[i+1]+1,ans[i])
        
        return sum(ans)
            
        