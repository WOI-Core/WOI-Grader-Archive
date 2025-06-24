
#include <iostream>
#include <vector>
#include <algorithm>

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
    int max_path = 1;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (i == 0 && j == 0) continue;

            int current_val = grid[i][j];

            if (i > 0 && grid[i-1][j] < current_val) {
                dp[i][j] = max(dp[i][j], dp[i-1][j] + 1);
            }
            if (j > 0 && grid[i][j-1] < current_val) {
                dp[i][j] = max(dp[i][j], dp[i][j-1] + 1);
            }
            
            if(dp[i][j] == 0){
                dp[i][j] = 1;
            }

            max_path = max(max_path, dp[i][j]);
        }
    }

    cout << max_path << endl;

    return 0;
}