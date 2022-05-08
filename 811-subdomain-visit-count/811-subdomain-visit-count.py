class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = collections.Counter()
        
        for domain in cpdomains:
            val,domain = domain.split()
            val = int(val)
            
            subdomains = domain.split(".")
            
            for i in range(len(subdomains)):
                ans[".".join(subdomains[i:])]+=val
            
            
        return ["{} {}".format(val,dom) for dom,val in ans.items()]
        
        