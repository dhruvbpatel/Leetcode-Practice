# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        d = defaultdict(list)
        
        q = [(root,0,0)]
        
        
        
        while(len(q)!=0):
            
            curr = q[0]
            q.pop(0)
            
            node = curr[0]
            v = curr[1]
            l = curr[2]
            
            if v not in d.keys():
                d[v] = defaultdict(list)
            
            d[v][l].append(node.val)
            
            if(node.left):
                q.append((node.left,v-1,l+1))
            
            if node.right:
                q.append((node.right,v+1,l+1))
        
        # print(d)
                
        ans = []
        
        d= dict(sorted(d.items()))
        # print(d)
        
        
        
         
        for v in d.keys():
            temp = []
            
            for l in d[v].keys():
                d[v][l].sort()
                temp.extend(d[v][l])
            
            ans.append(temp)
        
        return ans
            
        
        
        
        
            
            
            
                
            
            
        
        
        