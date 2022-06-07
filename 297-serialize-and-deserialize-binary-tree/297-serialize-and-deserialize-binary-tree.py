# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        if(root is None):
            return ""
        
        q = []
        q.append(root)
        s = ""
        
        while(len(q)>0):
            
            curr = q[0]
            q.pop(0)
            
            if(curr==None):
                s+="#,"
            else:
                s+=str(curr.val)
                s+=','
            
            if(curr is not None):
                q.append(curr.left)
                q.append(curr.right)
        
        print(s)
        return s
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        ## if string is null
        if(len(data)==0):
            return None
        
        start_idx = 0
        
        # get number value from string
        end_idx = data.find(',',start_idx)
        val = data[start_idx:end_idx]
        start_idx=end_idx+1
        
        print(val)
        
        root = TreeNode(int(val))
        q = []
        q.append(root)
        
        while(len(q)>0):
            
            node = q[0]
            q.pop(0)
            
            end_idx = data.find(',',start_idx)
            val = data[start_idx:end_idx]
            start_idx=end_idx+1
            
            if(val=='#'):
                node.left=None
            else:
                
                lnode = TreeNode(int(val))
                node.left = lnode
                q.append(lnode)
            
            end_idx = data.find(',',start_idx)
            val = data[start_idx:end_idx]
            start_idx=end_idx+1
            
            if(val=='#'):
                node.right=None
            else:
                
                rnode = TreeNode(int(val))
                node.right = rnode
                q.append(rnode)
        
        return root
            
            
            
            
        
        
        
        
        
        
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))