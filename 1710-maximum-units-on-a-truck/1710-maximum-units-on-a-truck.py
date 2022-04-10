class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], trucksize: int) -> int:
        
        boxTypes = sorted(boxTypes,key=lambda x:x[1],reverse=True)
        print(boxTypes)
        n = len(boxTypes)
        idx = 0
        
        ans = 0
        
        while(trucksize>0 and idx!=n):
            
            if(boxTypes[idx][0]<=trucksize):
                ans+=(boxTypes[idx][0]*boxTypes[idx][1])
                trucksize-=boxTypes[idx][0]
            else:
                
                ans+=trucksize*boxTypes[idx][1];
                trucksize-=trucksize
            
            idx+=1;
            
        return ans;