class Solution:
    def wordSubsets(self, A, B):
        cnt = Counter()
        
        for b in B:
            cnt |= Counter(b) #update cnt with max max freq value
        
        #after this cnt will have max freq with keys that form biggest subset
        # if this biggest subset is in word of A then that word is superset of b
        # to check superset, simply cnt-Counter(a), because cnt should be subset of A 
        # to satisfy conditon, if everything in cnt is in Counter(a) then 
        # cnt-counter(a) returns empty set even though counter(a) has some other chars
        # thus counter(a) is universal , so add to set
        
        
        return [a for a in A if not cnt - Counter(a)]  