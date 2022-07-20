class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        d = defaultdict(list)
        count = 0
        
        # dict structure
        # {
        #   "a": ["a", "acd", "ace"],
        #   "b": ["bb"]
        # }
        
        # for iterate over string and if that char is in dict, iterate over its list
        # and if any word len==1 then ans++ as it is completely traversed so subseq
        # else remove 1st char and update dict key with new key
        
        for word in words:
            d[word[0]].append(word)
        
        for char in s:
            
            curr_char_list = d[char]
            d[char]=[]
            
            for curr in curr_char_list:
                
                if len(curr)==1:
                    count+=1
                else:
                    d[curr[1]].append(curr[1:])
                
        return count
        