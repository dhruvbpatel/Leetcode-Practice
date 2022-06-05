class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        logic
        
          // every time check if number smaller than curr is in mp or not
        // if there then skip
        // if not then we have arrived at smallest number in possible sequence
        // then untill num++ is not in mp , increase val and check if in mp
        // also do count ,and max cout will be ans
                
        """
        
        
        st = set(nums)
        ans = 0
        
        
        for n in nums:
            
            if n-1 in st: #not smallest number so continue
                continue
            else:
                
                count = 1
                
                while(n+count in st):
                    count+=1
                    
                ans = max(count,ans)
        return ans

                
                
                

        