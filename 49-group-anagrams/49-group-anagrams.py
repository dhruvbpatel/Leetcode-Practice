class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        
        ans = []
        
        for s in strs:

            # sort_s = sorted(s)
            sort_s ="".join(sorted(s))
            mp[sort_s].append(s)
        
        
        for k in mp.keys():
            
            ans.append(mp[k])
        
        return ans
        