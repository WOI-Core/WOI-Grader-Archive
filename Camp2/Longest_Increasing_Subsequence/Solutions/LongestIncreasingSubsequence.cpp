
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    vector<int> dp;
    for (int num : arr) {
        if (dp.empty() || num > dp.back()) {
            dp.push_back(num);
        } else {
            *lower_bound(dp.begin(), dp.end(), num) = num;
        }
    }

    cout << dp.size() << endl;

    return 0;
}