class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s
        
        row = [""]*numRows
        
        back = True
        
        idx = 0
        
        for c in s:
            
            row[idx]+=c #add char in array
            
            if idx==0 or idx==numRows-1: # if 1st or last then reverse direction
                back = not back 
            
            if back: # if moving down 
                idx-=1
            else:
                idx+=1
        
        return "".join(row)