#include <bits/stdc++.h>
using namespace std;
#define ll long long

const int mxN = 3e2+10;

struct P {
    ll v, sum;
};

int n, T;
ll ans;
P dp[mxN][mxN];
int arr[mxN];

int main() {
    scanf("%d", &T);
    while(T--) {
        scanf("%d", &n);
        for(int i=0; i<n; ++i) scanf("%d", &arr[i]);
        for(int i=0; i<n; ++i) for(int j=0; j<n; j++) dp[i][j]=i==j?P{arr[i], 0}:P{(ll)1e18, (ll)1e18};
        for(int sz=1; sz<n; ++sz) {
            for(int l=0; l+sz<n; ++l) {
                int r = l+sz;
                for(int m=l; m<r; ++m) {
                    if(dp[l][r].sum<=dp[l][m].sum+dp[m+1][r].sum+dp[l][m].v*dp[m+1][r].v) continue;
                    dp[l][r].v = (dp[l][m].v+dp[m+1][r].v)%100, dp[l][r].sum = dp[l][m].sum+dp[m+1][r].sum+dp[l][m].v*dp[m+1][r].v;        
                }
            }
        }
        ans+=dp[0][n-1].sum;
    }
    printf("%lld", ans);
    return 0;
}