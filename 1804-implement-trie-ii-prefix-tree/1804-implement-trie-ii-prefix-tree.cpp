struct Node{
    Node* links[26];
    int ew=0;  // end with 
    int cp=0; // count prefix
    
    bool containsKey(char ch){
        return (links[ch-'a']!=NULL);
    }
    
    void put(char ch,Node* node){
        links[ch-'a'] = node;
    }
    
    Node* get(char ch){
        return links[ch-'a'];
    }
    
    
    
};

class Trie {
    
    private: Node* root;
    
    
public:
    Trie() {
        root = new Node();   
        // root->cp=0;
        // root->ew=0;
    }
    
    void insert(string word) {
        Node* node = root;
        
        for(int i=0;i<word.length();i++){
            if(!node->containsKey(word[i])){
                node->put(word[i],new Node());
            }
            node = node->get(word[i]);
            
            if(i==word.length()-1){
                node->ew+=1;
                node->cp+=1;
            }else{
                node->cp+=1;
            }
        }
    }
    
    int countWordsEqualTo(string word) {
        Node* node = root;
        
        for(int i=0;i<word.length();i++){
            if(node->containsKey(word[i])){
                node = node->get(word[i]);
            }else{
                return 0;
            }
        }
        
        return node->ew;
        
    }
    
    int countWordsStartingWith(string prefix) {
        Node* node = root;
        
        for(int i=0;i<prefix.length();i++){
            if(node->containsKey(prefix[i])){
                node =node->get(prefix[i]);
            }else{
                return 0;
            }
        }
        
        return node->cp;
    }
    
    void erase(string word) {
        Node* node = root;
        
        for(int i=0;i<word.length();i++){
            if(node->containsKey(word[i])){
               node=node->get(word[i]);
                node->cp-=1;
            }
        }
        node->ew-=1;
        
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * int param_2 = obj->countWordsEqualTo(word);
 * int param_3 = obj->countWordsStartingWith(prefix);
 * obj->erase(word);
 */