
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    vector<int> stones(n);
    for (int i = 0; i < n; ++i) {
        cin >> stones[i];
    }

    for (int i = 0; i < k; ++i) {
        int query;
        cin >> query;

        bool found = false;
        int left = 0, right = n - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (stones[mid] == query) {
                found = true;
                break;
            } else if (stones[mid] < query) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        if (found) {
            cout << "Yes" << endl;
        } else {
            cout << "No" << endl;
        }
    }

    return 0;
}