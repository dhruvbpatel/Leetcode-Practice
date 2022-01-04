class LRUCache {
public:
    
    class Node{
        public:
        
        int val;
        int key;
        
        Node* next;
        Node* prev;
        
        Node(int _key,int _val){
            val = _val;
            key = _key;
            
        }
        
    };
    
    Node* head = new Node(-1,-1);
    Node* tail = new Node(-1,-1);
    
    int cap;
    unordered_map<int,Node*> mp;
    
    
    LRUCache(int capacity) {
        cap = capacity;
        head->next = tail;
        tail->prev = head; // initialize dll
    }
    
    void addNode(Node* newnode){
        Node* nextnode = head->next;
        newnode->next = nextnode;
        newnode->prev = head;
        nextnode->prev = newnode;
        head->next = newnode;
    }
    
    void deleteNode(Node* delnode){
        
        Node* prevnode = delnode->prev;
        Node* nextnode = delnode->next;
        
        prevnode->next = nextnode;
        nextnode->prev = prevnode;
        
        
    }
    
    
    
    int get(int key) {
        
        if(mp.find(key)!=mp.end()){
            Node* nodeaddr  = mp[key];
            int nodeval = nodeaddr->val;
            mp.erase(key); // delete from hashmap;
            
            deleteNode(nodeaddr); // delete from ll;
            addNode(nodeaddr);  // add as most recent in ll
            
            mp[key]=head->next; //new address is head->next;
            return nodeval;   
        }
        else{
            return -1;  // not key in map;
        }
        
        
        
    }
    
    void put(int key, int value) {
        
        if(mp.find(key)!=mp.end()){ // if key is already in map
            
            Node* nodeaddr = mp[key]; // get addr
            mp.erase(key); // delete key from map
            deleteNode(nodeaddr); // delete node
            
        }
        if(mp.size()==cap){
            mp.erase(tail->prev->key); // delete prev of tail from map
            deleteNode(tail->prev); // delete node from ll
        }
        
        addNode(new Node(key,value));  // add node again
        mp[key] = head->next; // add key in map;
        
        
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */