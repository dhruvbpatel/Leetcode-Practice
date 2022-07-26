class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        
        for i in range(len(nums)-2):
            
            if(i==0 or (i>0 and nums[i]!=nums[i-1])):
                
                target = 0 - nums[i]
                
                low = i+1
                high = len(nums)-1
                
                while(low<high):
                    
                    if(nums[low]+nums[high]==target):
                        temp = []
                        temp.append(nums[i])
                        temp.append(nums[low])
                        temp.append(nums[high])
                        ans.append(temp)
                        
                        while(low<high and nums[low]==nums[low+1]):
                            low+=1
                        
                        while(low<high and nums[high]==nums[high-1]):
                            high-=1
                        
                        low+=1
                        high-=1
                    
                    elif(nums[low]+nums[high]<target):
                        low+=1
                    else:
                        high-=1
        
        return ans
                        
                            
                    
                    
                
        
        
        