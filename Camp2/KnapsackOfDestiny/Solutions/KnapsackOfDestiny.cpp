
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, W;
    cin >> n >> W;

    vector<int> weights(n);
    vector<int> values(n);

    for (int i = 0; i < n; ++i) {
        cin >> weights[i] >> values[i];
    }

    vector<vector<int>> dp(n + 1, vector<int>(W + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int w = 0; w <= W; ++w) {
            if (weights[i - 1] <= w) {
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w]);
            } else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    cout << dp[n][W] << endl;

    return 0;
}