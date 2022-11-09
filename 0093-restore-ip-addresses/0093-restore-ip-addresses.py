class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        ans = []
        #valid ip address will be maximum of 12 digits
        #because ip address has 4 integers seperated by dots in strings of max length 3
        #therefore 3*4=12
        if len(s)>12:
            return ans
        
        def dfs(i,dots,currIp):
            
            if dots>4:
                return
            
            if dots==4 and i==len(s):
                #currIp[:-1] to avoid trailing dots 
                ans.append(currIp[:-1])
                return
            
            
            for j in range(i,min(i+3,len(s))):
                #we will take min of i+3 and len as it will give list index out
                #of range error otherwise
                if int(s[i:j+1])<256 and (s[i]!="0" or i==j ):
                    dfs(j+1,dots+1,currIp+s[i:j+1]+".")
                    

                    
        dfs(0,0,"")
        
        return ans
        