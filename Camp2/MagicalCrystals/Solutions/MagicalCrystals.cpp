
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    vector<int> crystals(n);
    for (int i = 0; i < n; ++i) {
        cin >> crystals[i];
    }

    sort(crystals.begin(), crystals.end());

    int min_diff = INT_MAX;
    for (int i = 0; i <= n - k; ++i) {
        min_diff = min(min_diff, crystals[i + k - 1] - crystals[i]);
    }

    cout << min_diff << endl;

    return 0;
}