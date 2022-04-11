class Solution {
public:
    
   
    
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
        
        int m = grid.size();
        int n = grid[0].size();
        
        
        
        
        vector<vector<int>> ans(m,vector<int>(n,0));
        
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                
                // grid r,c to 1d array equivalent;
                
                int newidx = ((i*n+j)+k )%(n*m);  // formula is row*n + col; 
                
                int new_r = newidx/n;  // 1d array to equivalent row;
                int new_c = newidx%n;  // 1d array to equivalent col;
                
                               
                ans[new_r][new_c] = grid[i][j];
                
            }
        }
        
        
        return ans;
                                
        
    }
};