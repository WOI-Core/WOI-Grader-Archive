
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    vector<int> kingdoms(n);
    for (int i = 0; i < n; ++i) {
        cin >> kingdoms[i];
    }

    sort(kingdoms.begin(), kingdoms.end());

    cout << kingdoms[k - 1] << endl;

    return 0;
}