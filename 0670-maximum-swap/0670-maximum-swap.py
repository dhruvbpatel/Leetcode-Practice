class Solution:
    def maximumSwap(self, num: int) -> int:
        
        # Explanation
        # Basic idea:
        # Find a index i, where there is a increasing order
        # On the right side of i, find the max value (max_val) and its index (max_idx)
        # On the left side of i, find the most left value and its index (left_idx), which is less than max_val
        # Swap above left_idx and max_idx if necessary
        # Please check the comments for more detail
        
        s = list(str(num))
        
        n = len(s)
        
        flag = False
        
        for i in range(n-1):
            
            if s[i]<s[i+1]:
                flag = True
                break
        
        if flag==False:
            return num
        
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
            
        