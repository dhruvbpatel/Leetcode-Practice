class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        
        unordered_set<string> myset;
        bool isPresentWord = false;
        
        for(auto word:wordList){
            
            if(endWord.compare(word)==0){
                isPresentWord = true; // i/.e target word is in wordlist
            }
            
            myset.insert(word);
            
        }
        
        
        if(isPresentWord==false){ // endword is not in wordlist
            return 0;
        }
        
        queue<string> q;
        
        q.push(beginWord);
        
        int depth = 0;
        
        
        while(!q.empty()){
            depth++;
            
            int lsize = q.size(); // level size - no of element at each level
            
            while(lsize--){
                string curr = q.front();
                q.pop();
                
                // check all possible 1 depth words with transformation
                
                for(int i=0;i<curr.length();i++){ // for length of curr word
                    
                    string temp = curr;
                    
                    for(char c='a';c<='z';c++){ // for each index try all possible changes i.e 26 changes
                        temp[i] = c; // change ith index of temp
                        
                        if(curr.compare(temp)==0)
                            continue; // skip same word
                        
                        if(temp.compare(endWord)==0)
                            return depth+1; // after transformation we found endWord
                        
                        if(myset.find(temp)!=myset.end()){ //else if transformed word is in myset add it to q
                            q.push(temp);
                            myset.erase(temp);  // also erase from set
                        }
                    }
                }
            }
            
        }
    return 0;   
    }
};