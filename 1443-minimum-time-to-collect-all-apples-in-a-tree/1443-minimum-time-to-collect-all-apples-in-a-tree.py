class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        res: int = 0
        # edges.sort(key=lambda x: x[0])  not needed for the test cases
        # but is needed if the test cases included unsorted edges
        parents = [-1] * n
        seen = [False] * n
        seen[0] = True

        for a, b in edges:
            if seen[a] is True:
                parents[b] = a
            else:
                parents[a] = b

            seen[b] = True

        seen = [False] * n
        seen[0] = True

        for parent in range(1, n):  # 0 contributes no time regardless
            if hasApple[parent] is False:
                continue
            
            res += 1
            seen[parent] = True
            parent = parents[parent]
            while not seen[parent]:
                res += 1
                seen[parent] = True
                parent = parents[parent]
                          
        return 2 * res
