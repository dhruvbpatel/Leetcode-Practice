class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        num1 = -1
        num2 = -1
        c1 = 0
        c2 = 0
        
        for num in nums:
            
            if num==num1:
                c1+=1
            
            elif num==num2:
                c2+=1
            
            elif c1==0:
                num1=num
                c1+=1
            
            elif c2==0:
                num2=num
                c2+=1
            
            else:
                
                c1-=1
                c2-=1
                
        
        c1=c2=0
        
        for num in nums:
            if num==num1:c1+=1
            if num==num2:c2+=1
        
        target = len(nums)//3
        
        ans = []
        
        if c1>target: ans.append(num1)
        if c2>target and num1!=num2: ans.append(num2)
        
        return ans
        