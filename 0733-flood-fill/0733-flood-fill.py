class Solution:
    
    def fill(self,image,r,c,color,curr_color):
        
        
        if r<0 or c<0 or r>=len(image) or c>=len(image[0]) or image[r][c]!=curr_color:
            return
        
        if image[r][c]==color:
            return
        
        
        image[r][c]=color
        
        
        
        self.fill(image,r,c-1,color,curr_color)
        self.fill(image,r+1,c,color,curr_color)
        self.fill(image,r,c+1,color,curr_color)
        self.fill(image,r-1,c,color,curr_color)
        
        
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        m = len(image)
        n = len(image[0])
        
        if image[sr][sc]==color:
            return image
        
        
        curr_color = image[sr][sc]
        
        self.fill(image,sr,sc,color,curr_color)
        
        return image
        
        
        
        
        