class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
        hp = []
        
        heapq.heapify(hp)
        
        for i in nums:
            heapq.heappush(hp,int(i))
        
            if len(hp)>k:
                heapq.heappop(hp)
        
        return str(heapq.heappop(hp))