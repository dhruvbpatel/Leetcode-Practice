// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

vector<int> minAnd2ndMin(int a[], int n);

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int a[n];

        for (int i = 0; i < n; i++) 
            cin >> a[i];

        vector<int> ans = minAnd2ndMin(a, n);
        if (ans[0] == -1)
            cout << -1 << endl;
        else 
            cout << ans[0] << " " << ans[1] << endl;
    }
    return 0;
}// } Driver Code Ends


vector<int> minAnd2ndMin(int a[], int n) {
    
    int min1=-1;
    int min2=-1;
    
    for(int i=0;i<n;i++){
        
        if(min1==-1){
            min1 = a[i];
        }
        else if(min2==-1 and a[i]!=min1){
            if(a[i]<min1){
                swap(min1,min2);
                min1 = a[i];
            }else{
            
                min2 = a[i];

            }
        }else{
            
            if(a[i]<min2 and a[i]>min1){
                min2 = a[i];
            }else if(a[i]<min1){
                swap(min1,min2);
                min1 = a[i];
            }
        }
        
    }
    
    
    vector<int> ans;
    if(min1!=-1 and min2!=-1){
    ans.push_back(min1);
    ans.push_back(min2);
    return ans;
    }
    
    ans.push_back(-1);
    
    return ans;
}