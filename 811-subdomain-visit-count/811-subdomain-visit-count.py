def get_ans(mp):
        ans=[]

        for key in mp.keys():
            s = ""
            s+=str(mp[key])
            s+=str(" ")
            s+=key
            ans.append(s)

        return ans

class Solution:
    
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        mp={}

        for i in cpdomains:

            sp = i.split(" ")
            # print(sp)
            val = int(sp[0])
            domain = sp[1]

            if domain not in mp:
                mp[domain]=val
            else:
                mp[domain]+=val

            subdomain = domain.split(".")[1:]
            # print(subdomain)

            while(subdomain):
                key = ".".join(subdomain)

                if(len(subdomain)==1):
                    key = subdomain[-1]

                if key not in mp:
                    mp[key] = val
                else:
                    mp[key]+=val

                subdomain = subdomain[1:]

        return get_ans(mp)
        
    
        
        
            
            
            
            
            