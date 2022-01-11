class Solution {
public:
    
     void solveOptimised(int col,vector<string>& board,vector<vector<string>>& ans,
                       vector<int>& leftrow,
                        vector<int>& upperDiagonal,
                        vector<int>& lowerDiagonal, int n
                       ){
        
        if(col==n){
            ans.push_back(board);
            return;
        }
        
        
        for(int row = 0;row<n;row++){
            
            if(leftrow[row]==0 and 
              lowerDiagonal[row+col]== 0 and
               upperDiagonal[n-1+col-row] == 0){
                
                board[row][col]='Q';
                leftrow[row] =1;
                lowerDiagonal[row+col] = 1;
                upperDiagonal[n-1+col-row]=1;
                
                solveOptimised(col+1,board,ans,leftrow,upperDiagonal,lowerDiagonal,n);
                
                board[row][col]='.';
                leftrow[row] =0;
                lowerDiagonal[row+col] = 0;
                upperDiagonal[n-1+col-row]=0;
                
            }
            
            
        }
        
    }
    
    
    int totalNQueens(int n) {
        
         vector<vector<string>> ans;
        vector<string> board(n);
        
        string s(n,'.');
        
        for(int i=0;i<n;i++){
            board[i]=s;
        }
        
        // solve(0,board,ans,n); // old approach
        
        vector<int> leftrow(n,0);
        vector<int> upperDiagonal(2*n-1,0);
        vector<int> lowerDiagonal(2*n-1,0);
        
        solveOptimised(0,board,ans,leftrow,upperDiagonal,lowerDiagonal,n);
        
        
        return ans.size();
    }
};