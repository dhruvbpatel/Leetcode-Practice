class Solution:
    
        
    def helper(self,image,r,c,color,m,n,start):

        if r<0 or r>=m or c<0 or c>=n or image[r][c]!=start:
            return
            
        
        if image[r][c]==start:
            image[r][c]=color

        self.helper(image,r+1,c,color,m,n,start)
        self.helper(image,r-1,c,color,m,n,start)
        self.helper(image,r,c-1,color,m,n,start)
        self.helper(image,r,c+1,color,m,n,start)
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        m=len(image)
        n=len(image[0])

        start = image[sr][sc]

        if start==color:
            return image

        self.helper(image,sr,sc,color,m,n,start)

        return image
        
        