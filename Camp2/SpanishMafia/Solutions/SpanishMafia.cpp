#include <bits/stdc++.h>
using namespace std;
#define ll long long

const int mxN = 3e2+10;

// Structure to hold both the resulting value (v) and the minimum cost (sum)
struct P {
    ll v, sum;
};

int n, T;
ll ans;
P dp[mxN][mxN];
int arr[mxN];

int main() {
    // This solution uses scanf, which is faster for large inputs
    scanf("%d", &T);
    while(T--) {
        scanf("%d", &n);
        for(int i=0; i<n; ++i) scanf("%d", &arr[i]);

        // Initialize DP table
        for(int i=0; i<n; ++i) {
            for(int j=0; j<n; j++) {
                // Base case: a single item has its own value and 0 cost to merge
                if (i == j) {
                    dp[i][j] = P{(ll)arr[i], 0};
                } else {
                    // Initialize other states with a very large cost
                    dp[i][j] = P{(ll)1e18, (ll)1e18};
                }
            }
        }

        // DP loop for Matrix Chain Multiplication
        // sz is the length of the chain being considered
        for(int sz=1; sz<n; ++sz) {
            // l is the starting index of the chain
            for(int l=0; l+sz<n; ++l) {
                // r is the ending index of the chain
                int r = l+sz;
                // m is the split point
                for(int m=l; m<r; ++m) {
                    ll current_cost = dp[l][m].sum + dp[m+1][r].sum + dp[l][m].v * dp[m+1][r].v;
                    // If we found a cheaper way to merge the chain [l, r]
                    if(dp[l][r].sum > current_cost) {
                         dp[l][r].sum = current_cost;
                         dp[l][r].v = (dp[l][m].v + dp[m+1][r].v) % 100;
                    }
                }
            }
        }
        // Add the minimum cost for this test case to the total answer
        ans += dp[0][n-1].sum;
    }
    printf("%lld", ans);
    return 0;
}
