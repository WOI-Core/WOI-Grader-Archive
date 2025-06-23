#include <bits/stdc++.h>
using namespace std;

const int mxN = 1e5+10;
const int mxM = 1e4+10;

stack<int> st[mxM];

bool isNotAvailable[mxM];

int main() {
    int n, m; 
    
    cin >> n >> m;
    
    for(int i=0; i<n; i++) {
        int tmp;
        cin >> tmp;
        st[1+(i%m)].push(tmp);
    }
    
    int T; 
    cin >> T;
    
    while(T--) {
        
        int x, k; 
        cin >> x >> k;
        
        isNotAvailable[x] = true;
        
        while(st[x].size() > k) {
            
            int mn = 1e9, tar = 0, mn_gap = 1e9;
            
            for(int i=1; i<=m; i++) {
                
                if( st[i].size() <= mn && !isNotAvailable[i] ) {
                    
                    if( st[i].size() < mn || st[i].size() == mn && abs(x-i) < mn_gap ) {
                        
                        mn_gap = abs(x-i);
                        mn = st[i].size();
                        tar = i;
                        
                    }
                    
                }
                
            }
            
            st[tar].push(st[x].top());
            st[x].pop();
            
        }
    }
    
    for(int i=1; i<=m; i++) {
        
        int sum = 0;
        
        while(!st[i].empty()) {
            sum += st[i].top();
            st[i].pop();
        }
        
        cout << sum << "\n";
        
    }
    
    return 0;
}