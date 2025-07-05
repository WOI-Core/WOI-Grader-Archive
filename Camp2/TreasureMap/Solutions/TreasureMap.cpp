
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, m, k;
    cin >> n >> m >> k;

    vector<vector<int>> grid(n, vector<int>(m));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> grid[i][j];
        }
    }

    vector<int> values;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            values.push_back(grid[i][j]);
        }
    }

    sort(values.begin(), values.end());

    int sum = 0;
    for (int i = 0; i < k; ++i) {
        sum += values[i];
    }

    cout << sum << endl;

    return 0;
}