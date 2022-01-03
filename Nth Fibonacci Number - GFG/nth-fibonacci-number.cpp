// { Driver Code Starts
// Initial Template for C++
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
// User function Template for C++
#define md 10e9+7
class Solution {
  public:
    long long int nthFibonacci(long long int n){
        // code here
        vector<long long int> dp(n+1);
        
        dp[0]=0;
        dp[1]=1;
        
        for(long long int i=2;i<n+1;i++){
            dp[i] = (dp[i-1]+dp[i-2])%1000000007;
            
        }
        
        return dp[n];
        
        
    }
};

// { Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        long long int n;
        cin >> n;
        Solution ob;
        cout << ob.nthFibonacci(n) << endl;
    }
    return 0;
}
  // } Driver Code Ends