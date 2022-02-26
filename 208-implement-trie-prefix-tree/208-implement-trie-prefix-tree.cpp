
struct Node{
    Node* links[26];
    bool flag = false;
    
    bool containsKey(char ch){
        return (links[ch-'a']!=NULL);  //check if link has node
    }
    
    void put(char ch,Node* node){
        links[ch-'a'] = node;  // put ref link in char 
    }
    
    Node* get(char ch){
        return links[ch-'a'];
    }
    
    void setEnd(){
        flag = true;
    }
    
    bool isEnd(){
        return flag;
    }
    
    
};

class Trie {
    private: Node* root;
    
public:
    Trie() {
        root = new Node(); // initialize
    }
    
    void insert(string word) {
        Node* node=root;  // initialize a node
        
        for(int i=0;i<word.length();i++){  // for each char in word
            if(!node->containsKey(word[i])){  // check if char is in node
                node->put(word[i],new Node());  // if not put in node and create new ref node
            }
            
            node = node->get(word[i]);      // move to next node    
        }
        
        node->setEnd(); // when word is traversed, mark as end
    }
    
    bool search(string word) {
        Node* node = root;
        
        for(int i=0;i<word.length();i++){
            if(!node->containsKey(word[i])){
                return false;  // if char is not present then word is not present
            }
            node = node->get(word[i]);  // move to next node
        }
        
        if(node->isEnd()){ // if all char is traversed and if node is ended then true
            return true;
        }
        
        return false; // else false
    }
    
    bool startsWith(string prefix) {
        Node* node = root;
        for(int i=0;i<prefix.size();i++){
            if(!node->containsKey(prefix[i])){
                return false;  // only if word is left and char is not then false
            }
            
            node = node->get(prefix[i]); // move to next node
        }
        
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */