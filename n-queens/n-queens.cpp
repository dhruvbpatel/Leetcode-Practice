class Solution {
public:
    bool isSafe(int row,int col,vector<string>& board,int n){
        
        int r = row;
        int c = col;
        
        // check diagonally;
        while(row>=0 and col>=0){
            if(board[row][col]=='Q') return false;
            row--;
            col--;
        }
        
        row = r;
        col = c;
        while(col>=0){
            if(board[row][col]=='Q') return false; // check left size horizonatally
            // row++;
            col--;
        }
        
        row = r;
        col =c ;
        
        while(row<n and col>=0){
            if(board[row][col]=='Q') return false;
            row++;
            col--;
        }
        
        return true;
        
    }
    
    
    void solve(int col,vector<string>& board,vector<vector<string>>& ans,int n){
        
        if(col==n){ // column exceeded our limit then we have successfully arrived to solution
            ans.push_back(board);
            return;
        }
        // cout<<"a";
        for(int row=0;row<n;row++){
            
            if(isSafe(row,col,board,n)){
                board[row][col]='Q';
                solve(col+1,board,ans,n);
                board[row][col]='.';
            }
            
        }
        
    }
    
       
    
    vector<vector<string>> solveNQueens(int n) {
        
        vector<vector<string>> ans;
        vector<string> board(n);
        
        string s(n,'.');
        
        for(int i=0;i<n;i++){
            board[i]=s;
        }
        
        solve(0,board,ans,n);
        return ans;
        
    }
};