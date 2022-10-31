class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        for r in range(1,len(matrix)):
            for c in range(1,len(matrix[0])):
                if matrix[r-1][c-1]!=matrix[r][c]:
                    return False
        
        return True
        
#         groups = {}
        
#         for r,row in enumerate(matrix):
#             for c,val in enumerate(row):
                
#                 if r-c not in groups:
#                     groups[r-c]=val
#                 else:
#                     if groups[r-c]!=val:
#                         return False
#         return True

        
        