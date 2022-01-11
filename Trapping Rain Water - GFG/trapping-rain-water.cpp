// { Driver Code Starts
#include<bits/stdc++.h>

using namespace std;


 // } Driver Code Ends
class Solution{
typedef long long ll;
    // Function to find the trapped water between the blocks.
    public:
    long long trappingWater(int arr[], int n){
        // code here
        
        long long  leftmax = 0, rightmax = 0;
        int l = 0;
        int r = n-1;
        
        ll ans = 0;
        
        while(l<=r){
            
            if(arr[l]<=arr[r]){
                
                if(arr[l]>=leftmax){
                    leftmax = arr[l];
                }else{
                    
                    ans+=leftmax - arr[l];
                    
                }
                
                l++;
            }else{
                // if arr[r]>arr[l]
                
                if(arr[r]>=rightmax){
                    rightmax = arr[r];
                }else{
                    ans+=rightmax-arr[r];
                }
                
                r--;
            }
            
        }
        return ans;
    }
};

// { Driver Code Starts.

int main(){
    
    int t;
    //testcases
    cin >> t;
    
    while(t--){
        int n;
        
        //size of array
        cin >> n;
        
        int a[n];
        
        //adding elements to the array
        for(int i =0;i<n;i++){
            cin >> a[i];            
        }
        Solution obj;
        //calling trappingWater() function
        cout << obj.trappingWater(a, n) << endl;
        
    }
    
    return 0;
}  // } Driver Code Ends