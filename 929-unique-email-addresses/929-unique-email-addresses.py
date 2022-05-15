class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        ans = set()
        
        for email in emails:
            
            name, domain = email.split('@')
            local = name.split('+')[0].replace('.','')
            
            ans.add(local+'@'+domain)
        
        return len(ans)
            