/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is lower than the guess number
 *			      1 if num is higher than the guess number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    typedef long long ll;
    int solve(ll l,ll r){
        
        while(l<=r){
            
            ll mid = l+(r-l)/2;
            
            ll ans = guess(mid);
            
            if(ans==0) return mid;
            else if(ans==1){
                l = mid+1;
            }
            else r = mid-1;
        }
        
        return l;
        
    }
    
    int guessNumber(int n) {
        
        if(n==1) return 1;
        return solve(1,n);
    }
};