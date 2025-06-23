#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const int N_MAX = 1001;
const int SUM_MAX = 5001;
const int MOD = 1e9+7;
const int OFFSET = 2500; // Offset to handle negative sums

ll dp[N_MAX][SUM_MAX];
int A[N_MAX];
int n;
ll k;

ll solve(int i, ll current_sum_offset) {
    if (i == n) {
        // Compare the real sum with k
        return (current_sum_offset - OFFSET) == k;
    }
    // Check if this state has been computed
    if (dp[i][current_sum_offset] != -1) {
        return dp[i][current_sum_offset];
    }

    // Recur for both + and - operations
    ll add_case = solve(i + 1, current_sum_offset + A[i]);
    ll subtract_case = solve(i + 1, current_sum_offset - A[i]);

    // Store and return the result
    return dp[i][current_sum_offset] = (add_case + subtract_case) % MOD;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n >> k;
    memset(dp, -1, sizeof(dp));
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }

    // Start recursion with the initial sum of 0, plus the offset
    cout << solve(0, OFFSET);

    return 0;
}
