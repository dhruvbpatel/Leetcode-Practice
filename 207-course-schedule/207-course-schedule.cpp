class Solution {
public:
    
    // 2 - > processing , 1-> processed, 0 ->not visited
    
    bool isCyclic( vector<vector<int>>& adj,vector<int>& visited,int curr){
        
        if(visited[curr]==2){
            return true;  // then cycle is there as u reach node which is processing 
        }
        
        visited[curr]=2; // not processing make it 
        
        for(int i=0;i<adj[curr].size();i++){
            if(visited[adj[curr][i]]!=1){  // skipping already processed nodes
                if(isCyclic(adj,visited,adj[curr][i]))
                    return true;
            } 
        }   
        
        visited[curr]=1;
        return false;
    }
    
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        
        vector<vector<int>> adj(numCourses);
        
        for(int i =0;i<prerequisites.size();i++){
            adj[prerequisites[i][0]].push_back(prerequisites[i][1]);
        }
          
        vector<int> visited(numCourses,0);
        
        for(int i =0;i<numCourses;i++){
            if(visited[i]==0){
                if(isCyclic(adj,visited,i)){
                    return false;
                }
            }
        }
        
        return true;
        
        
    }
};