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
    
    
    bool isBipartite(vector<vector<int>>& graph) {
        
        int n = graph.size();
        
        vector<int> color(n,-1); // color array, -1 means uncolored
        
        for(int i=0;i<n;i++){
            if(color[i]==-1){ // if uncolored
                if(!isBipartite(i,color,graph)){  // bfs and color it and check for cycle
                    return false; 
                }
            }
        }
        
        return true;
        
    }
};