class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        
        vector<vector<int>> arr(n,vector<int>(n,1));
        
        
        int row_start = 0,row_end = n-1, col_start =0,col_end = n-1;
        
        int val = 1;
        
        while(row_start<=row_end and col_start<=col_end){
            
            
            for(int i = col_start; i<=col_end;i++ ){
                arr[row_start][i] = val++;
            }
            row_start++;
            
            
            
            for(int i= row_start;i<=row_end;i++){
                arr[i][col_end] = val++;
            }
            col_end--;
            
            
            if(row_end>=row_start){
                
                
                for(int i = col_end;i>=col_start;i--){
                    
                    arr[row_end][i]=val++;
                    
                }
                
                row_end--;
                
            }
            
            
            if(col_end>=col_start){
                
                
                for(int i =row_end;i>=row_start;i--){
                    arr[i][col_start]= val++;
                }
                
                col_start++;
            }   
            
            
        }
     
        return arr;
        
    }
};