class Solution {
public:
    
    bool dfs(vector<vector<char>>& board,string& word,int r,int c,int wp,int nrow,int ncol,
             vector<vector<int>>& temp){
        
        if(wp==word.size()) return true;
        
        if(r<0 or r>=nrow or c<0 or c>=ncol or word[wp]!=board[r][c] or temp[r][c]==-1){
            return false;
        }
        
        temp[r][c]=-1;
        
        bool ans = dfs(board,word,r+1,c,wp+1,nrow,ncol,temp)
            or dfs(board,word,r-1,c,wp+1,nrow,ncol,temp)
            or dfs(board,word,r,c+1,wp+1,nrow,ncol,temp)
            or dfs(board,word,r,c-1,wp+1,nrow,ncol,temp); 
        
        temp[r][c]=0;
        return ans;
                    
    }
    
    
    
    bool exist(vector<vector<char>>& board, string word) {
        
        int nrow = board.size();
        int ncol = board[0].size();
        
        vector<vector<int>> temp(nrow,vector<int>(ncol,0)); // to mark visited position
        
        int wp = 0; // word pointer;
        
        for(int i=0;i<nrow;i++){
            for(int j=0;j<ncol;j++){
                if(dfs(board,word,i,j,0,nrow,ncol,temp)) return true;
            }
        }
        
        return false;
        
        // time complexity -> (n*m * (4^n)(dfs is calling 4 recursive max n times))
        
        
    }
};