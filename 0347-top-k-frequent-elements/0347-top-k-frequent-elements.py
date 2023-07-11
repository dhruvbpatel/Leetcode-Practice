from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        hp = []
        heapq.heapify(hp)
        
        d=defaultdict(int)
        
        for i in nums:
            d[i]+=1 
            
        
        for ky,v in d.items():
            
            heapq.heappush(hp,[v,ky])
            
            if len(hp)>k:
                heapq.heappop(hp)
            
        # print(hp)
        ans=[]
        
        while hp:
            ans.append(heapq.heappop(hp)[1])
        
        return ans
        
        