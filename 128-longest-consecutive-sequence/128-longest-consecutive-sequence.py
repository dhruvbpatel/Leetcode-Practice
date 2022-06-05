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
        
        
        n = len(nums)
        
        if n==1 or n==0:
            return n
        
        mp = defaultdict(int)
        
        for ele in nums:
            mp[ele]+=1
        
        ans = 0
        
        for ele in nums:
            
            if mp[ele-1]>0:
                continue
            else:
                
                # curr = curr+1
                count = 0
                curr = ele
                
                while(mp[curr]!=0):
                    
                    count+=1
                    curr+=1
                    
                ans = max(count,ans)
        
        return ans
                    
                

        