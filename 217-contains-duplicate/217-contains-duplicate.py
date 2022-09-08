class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        st = set()
        
        for ele in nums:
            
            if ele in st:
                return True
            else:
                st.add(ele)
        
        return False
        