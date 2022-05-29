class Solution:
    
    def check(self,s,start,end):
        # end = len(s)-1
        while(start<=end):
            
            if(s[start]!=s[end]):
                return False
            
            start+=1
            end-=1
            
        return True

    def solve(self,s,idx,temp,ans):
        
        if(idx==len(s)):
            ans.append(list(temp))
            return
        
        for i in range(idx,len(s)):
            
            if(self.check(s,idx,i)):
                temp.append(s[idx:i+1])
                self.solve(s,i+1,temp,ans)
                temp.pop(-1)
        
        return
                
    
    def partition(self, s: str) -> List[List[str]]:
        idx = 0
        temp = []
        ans = []
        self.solve(s,idx,temp,ans);
        return ans;
        