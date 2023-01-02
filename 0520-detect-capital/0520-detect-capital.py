class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        n = len(word)
        
        if n==1:
            return True
        
        # all capital
        if word[0].isupper() and word[1].isupper():
            for i in range(2,n):
                if not word[i].isupper():
                    return False
        
        else:
            # first capital and all lower
            for i in range(1,n):
                if word[i].isupper():
                    return False
        
        return True
        