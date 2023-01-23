class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        if len(trust)==0 and n==1:
            return n
        
        if n>1 and len(trust)==0:
            return -1
        
        d = defaultdict(int)
        
        in_degree = [0]*(n+1)
        
        for x,y in trust:
            in_degree[y]+=1
            d[x]+=1
            
        
        for i in range(len(in_degree)):
            if in_degree[i]==n-1 and d[i]==0:
                return i
        
        return -1
        
        
        