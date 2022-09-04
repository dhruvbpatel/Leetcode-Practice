# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        d = defaultdict(list) ## create data structure of
        
        q = [(root,0,0)] # queue
        # node,vertical-level, depth-level
        #node,v,l
        
        while(len(q)!=0):
            
            curr = q[0]
            q.pop(0)
            
            node = curr[0]
            v = curr[1]
            l = curr[2]
            
            if v not in d.keys(): # if v not in d, create dict of dict for v
                d[v] = defaultdict(list)
            
            d[v][l].append(node.val) # add node with main key as v and level as subkey
            
            if(node.left):
                q.append((node.left,v-1,l+1)) # add left right child
            
            if node.right:
                q.append((node.right,v+1,l+1))
        
        # print(d)
                
        ans = []
        
        d= dict(sorted(d.items())) # sort dict acc to main key i.e vertical
        # print(d)

        for v in d.keys(): #iterate over verticl
            
            temp = []
            
            for l in d[v].keys(): # in vertical iterate over level
                d[v][l].sort() # sort the node value in list on same level
                temp.extend(d[v][l])
            
            ans.append(temp)
        
        return ans
            
        
        
        
        
            
            
            
                
            
            
        
        
        