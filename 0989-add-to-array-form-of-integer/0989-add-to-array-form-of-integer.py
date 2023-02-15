class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        l1 = len(num)
        l2 = len(str(k))
        
        ans = [0]*(max(l1,l2)+1)
        
        carry = 0
        ks = str(k)
        
        i = l1-1
        j = l2-1
        k = len(ans)-1
        
        while i>=0 or j>=0 or carry:
            
            curr = 0
            
            if i>=0 and j>=0:
                curr+=num[i]+int(ks[j])
                
            elif i>=0:
                curr+=num[i]
            elif j>=0:
                curr+=int(ks[j])
            
            curr+=carry
            # print(i)
            carry=curr//10
            
            ans[k]=curr%10
            
            i-=1
            j-=1
            k-=1
        
        return ans if ans[0]!=0 else ans[1:]
                
            
            
        
        
#         274
#         181
#         0455