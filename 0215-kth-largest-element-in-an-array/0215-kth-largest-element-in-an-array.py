class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        hp = []
        heapq.heapify(hp)
        
        for i in nums:
            heapq.heappush(hp,i)
            
            if len(hp)>k:
                heapq.heappop(hp)
        
        return heapq.heappop(hp)
        
        # return heapq.nlargest(k,nums)[-1]