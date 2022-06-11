# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return None
        
        d = defaultdict(list) # v->l->node
        
        q = [(root,0,0)] # node, vertical-level, depth-level
        
        while(len(q)!=0):
            
            curr = q[0]
            q.pop(0)
            
            node = curr[0]
            v = curr[1]
            l = curr[2]
            
            if v not in d.keys():
                d[v] = defaultdict(list)
            
            d[v][l].append(node.val)
            
            if node.left:
                q.append((node.left,v-1,l+1))
            
            if node.right:
                q.append((node.right,v+1,l+1))
        
        
        ans = []
        
        d = dict(sorted(d.items()))
        
        for v in d.keys():
            temp = []
            
            for l in d[v].keys():
                # d[v][l].sort() # only change is no sort required
                temp.extend(d[v][l])
            
            ans.append(temp)
        
        return ans
            
        