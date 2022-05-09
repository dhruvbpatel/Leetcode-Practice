from collections import deque
class Solution:
    def findCircleNum(self, m: List[List[int]]) -> int:
        visited = set()
        
        ans = 0
        
        for i in range(len(m)):
            if i not in visited:
                visited.add(i)
                q = deque()
                q.append(i)
                
                while(q):
                    curr = q.popleft()
                    for j in range(len(m[curr])):
                        if j not in visited and m[curr][j]==1:
                            visited.add(j)
                            q.append(j)
                ans+=1
        return ans
                
                

                
                
            
                
        