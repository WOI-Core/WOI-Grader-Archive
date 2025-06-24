
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    sort(a.begin(), a.end());

    vector<vector<long long>> dp(n + 1, vector<long long>(k + 1, LLONG_MAX));
    dp[0][0] = 0;

    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j <= k; ++j) {
            dp[i][j] = dp[i - 1][j]; 
            if (i >= 2 && j >= 1 && dp[i - 2][j - 1] != LLONG_MAX) {
                dp[i][j] = min(dp[i][j], dp[i - 2][j - 1] + (long long)(a[i - 1] - a[i - 2]) * (a[i - 1] - a[i - 2]));
            }
        }
    }

    cout << dp[n][k] << endl;

    return 0;
}