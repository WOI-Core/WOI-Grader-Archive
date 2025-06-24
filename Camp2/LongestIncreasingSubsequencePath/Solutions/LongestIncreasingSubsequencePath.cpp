
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<vector<int>> grid(n, vector<int>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> grid[i][j];
        }
    }

    vector<vector<int>> dp(n, vector<int>(n, 0));
    dp[0][0] = 1;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (i + 1 < n && grid[i + 1][j] > grid[i][j]) {
                dp[i + 1][j] += dp[i][j];
            }
            if (j + 1 < n && grid[i][j + 1] > grid[i][j]) {
                dp[i][j + 1] += dp[i][j];
            }
        }
    }

    cout << dp[n - 1][n - 1] << endl;

    return 0;
}