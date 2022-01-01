class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
        items.sort(key = lambda x:x[0]) # get the 1st element in sorted 
        items.sort(key = lambda x:x[1],reverse=True)
        ans = []
        
        d={}
        
        for i in items:
            if i[0] not in d.keys():
                d[i[0]] = []
                d[i[0]].append(i[1])
            
            elif len(d[i[0]])<5:
                d[i[0]].append(i[1])
            else:
                continue
        
        
        for key in d:
            temp =[key,int(mean(d[key]))]
            ans.append(temp)
        
        
        # print(d)
        ans.sort(key = lambda x:x[0])
        return ans
        
        
        
        
        
        
        
        