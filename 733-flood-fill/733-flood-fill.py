class Solution:
    
    def fill(self,image,r,c,color,start):
        
        if r<0 or c<0 or r>=len(image) or c>=len(image[0]) or image[r][c]!=start:
            return
        
        if image[r][c]==start:
            image[r][c]=color
        
        self.fill(image,r+1,c,color,start)
        self.fill(image,r,c+1,color,start)
        self.fill(image,r,c-1,color,start)
        self.fill(image,r-1,c,color,start)
    
        
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        m = len(image)
        n = len(image[0])
        
        start = image[sr][sc]
        
        if start==color:
            return image
        
        r = sr
        c = sc
        
        self.fill(image,sr,sc,color,start)
        
        return image
        