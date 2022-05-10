class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans = []
        
        for i in range(len(nums)-2):
            
            if(i==0 or (i>0 and nums[i]!=nums[i-1])):
                
                low = i+1
                high = len(nums)-1
                temp = 0-nums[i]
                
                while(low<high):
                    
                    if(nums[low]+nums[high]==temp):
                        
                        t = []
                        t.append(nums[i])
                        t.append(nums[low])
                        t.append(nums[high])
                        ans.append(t)
                        
                        while(low<high and nums[low]==nums[low+1]):
                            low+=1
                        
                        while(low<high and nums[high]==nums[high-1]):
                            high-=1
                            
                        low+=1
                        high-=1
                        
                        
                    elif(nums[low]+nums[high]<temp):
                        low+=1
                    else:
                        high-=1
        return ans
                    
                        
                
                
            
            
        