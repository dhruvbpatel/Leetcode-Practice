class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits)==0:
            return []
        
        
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        
                
        def find(idx,temp):
            
            if len(temp)==len(digits):
                ans.append("".join(temp))
                return
        
            possible_letters = letters[digits[idx]]
            
            for letter in possible_letters:
                temp.append(letter)
                find(idx+1,temp)
                temp.pop()
                
        ans = []
        find(0,[])
        return ans