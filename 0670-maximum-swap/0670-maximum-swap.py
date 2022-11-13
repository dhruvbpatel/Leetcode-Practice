class Solution:
    def maximumSwap(self, num: int) -> int:
        
        s = list(str(num))
        
        n = len(s)
        
        for i in range(n-1):
            
            if s[i]<s[i+1]:
                break
        
        else: return num
        
        mx_idx,mx_val = i+1,s[i+1]
        
        for j in range(i+1,n):
            if s[j]>=mx_val:
                mx_idx , mx_val = j,s[j]
        
        left_idx = i
        
        for j in range(i,-1,-1):
            if s[j]<mx_val:
                left_idx = j
        
        s[mx_idx],s[left_idx] = s[left_idx],s[mx_idx]
        
        return int("".join(s))
            
        