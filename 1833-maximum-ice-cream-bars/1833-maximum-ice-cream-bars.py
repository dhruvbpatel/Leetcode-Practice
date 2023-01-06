class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        costs.sort()
        
        count = 0
        
        for curr in costs:
            if coins<curr:
                break
            else:
                coins-=curr
                count+=1
        
        return count
        