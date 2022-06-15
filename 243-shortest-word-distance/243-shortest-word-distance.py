class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        
        wp1 = -1
        wp2 = -1
        
        ans = len(wordsDict)
        
        for i in range(len(wordsDict)):
            
            if wordsDict[i]==word1:
                wp1 = i
            
            elif wordsDict[i] == word2:
                wp2 = i
            
            
            if wp1!=-1 and wp2!=-1:
                ans = min(ans,abs(wp2-wp1))
        
        return ans
        