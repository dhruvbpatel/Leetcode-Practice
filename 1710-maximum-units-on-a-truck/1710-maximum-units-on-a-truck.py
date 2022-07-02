class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], trucksize: int) -> int:
        
        bt = sorted(boxTypes,key = lambda x:x[1],reverse=True)
        # print(bt)
        ans = 0
        idx = 0
        
        while idx<len(bt) and trucksize!=0:
            
            if bt[idx][0]<=trucksize:
                ans += (bt[idx][0]*bt[idx][1])
                trucksize-=bt[idx][0]
            
            else:
                ans += trucksize*bt[idx][1]
                break
                
            idx+=1
        return ans
            
            
            
        
        
        
        