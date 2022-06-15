class WordDistance:

    def __init__(self, words: List[str]):
        self.mp = dict()
        self.len = len(words)
        
        # mp with key as word and value as list of index of occurence
        
        for i in range(len(words)):
            
            if self.mp.get(words[i]) is None:
                self.mp[words[i]] = [i]
            
            self.mp[words[i]] = self.mp[words[i]]+[i] ## append index in mp

    def shortest(self, word1: str, word2: str) -> int:
        
        w1_idx_list = self.mp.get(word1)
        w2_idx_list = self.mp.get(word2)
        
        ans = self.len
        
        for i in w1_idx_list:
            for j in w2_idx_list:
                
                ans = min(ans,abs(i-j))
        
        return ans
                
                


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)