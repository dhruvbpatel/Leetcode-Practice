class Solution {
public:
    bool isBipartite(int src,vector<int>& color,vector<vector<int>>& graph){
        queue<int> q; 
        q.push(src);// initially push 1st node;
        color[src]=1; // color 1st node as 1
        
        while(!q.empty()){
            int node = q.front();  
            q.pop();
            
            for(auto it:graph[node]){  // iterate to 1st nodes adjacent
                if(color[it]==-1){ // if uncolored , color it
                    color[it] = 1 - color[node]; // mark as opposite color if unmarked;
                    q.push(it);// push adjacent nodes in queue
                }else if(color[it]==color[node]){ // it adjacent is already with same color , not bipartite
                    return false; // return false as it is not
                }
            }
        }
        
        return true;  // if all color is done ,it is bipartite
    }
    
    bool dfs(int node,vector<int>& color,vector<vector<int>>& graph){
        
        
        if(color[node]==-1) color[node]=1;
        
        for(auto it:graph[node]){
            if(color[it]==-1){
                color[it] = 1-color[node];
                if(!dfs(it,color,graph)){
                    return false;
                }
                
            }else if(color[it]==color[node]){
                return false;
            }
        }
        
        return true;
        
        
    }
    
    bool isBipartite(vector<vector<int>>& graph) {
        
        int n = graph.size();
        
        vector<int> color(n,-1); // color array, -1 means uncolored
        
        for(int i=0;i<n;i++){
            if(color[i]==-1){ // if uncolored
                
                //bfs
                // if(!isBipartite(i,color,graph)){  // bfs and color it and check for cycle
                //     return false; 
                // }
                
                //dfs
                if(!dfs(i,color,graph)){
                    return false;
                }
                
                
            }
        }
        
        return true;
        
    }
};