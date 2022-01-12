#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    string fractionAddition(string expression) {
        
        istringstream ss(expression); // int string reader, reads interger from strings
        
        int A = 0, B = 1 ,a , b;// store final ans afer each iteration in numerator A and denominator B;
        
        char _; // wildcard char reader
        
        while(ss>>a>>_>>b){ // read integer inputs in a and b 
            cout<<a<<" "<<_<<" "<<b<<endl;
            
            A = A*b+B*a;
            B = B*b;
            
            int gcd = abs(__gcd(A,B));
            
            // cout<<gcd<<endl;
            
            A = A/gcd;
            B = B/gcd;
            
        }
        
        return to_string(A) + '/' + to_string(B);
        
        
        
        
    }
};