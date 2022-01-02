class Solution {
public:
    int numTeams(vector<int>& rating) {
        
        
//         // idea is to fix j and check to left and right
//         We start a j loop between 1...n-1 to check all valid positions to fix j.
// At every such position, we check how many elements towards the left are smaller than j and how many such elements are greater than j i.e count of i<j & count of i>j
// Similarly, we check how many elements towards the right of j are greater than j (j<k) and how many such elements are smaller than j (k>j)
        //After we get this count, the answer for that particular position of j will be :-
// (count of i<j * count of j<k) + (count of i>j * count of j>k)
// Thus this comes down to :- answer += (i_smaller * k_larger + i_larger * k_smaller);
        
        int n = rating.size();
        
        int ans = 0;
        
        for(int j=0;j<n;j++){ // fix j
            
            int i_small =0, i_large = 0, k_small = 0, k_large = 0;
            
            for(int i=0;i<j;i++){ /// check towards j's left 
                
                if(rating[i]<rating[j]){
                    i_small++;
                    
                }else if(rating[i]>rating[j]){
                    
                    i_large++;
                }
            }
            
            for(int k=j+1;k<n;k++){ // check toward j's right
                
                if(rating[j]<rating[k]){
                    k_large++;
                    
                }else if(rating[j]>rating[k]){
                    k_small++;
                }
            }
            
            ans+= i_small*k_large + i_large*k_small;
        }
        return ans;
        
    }
};