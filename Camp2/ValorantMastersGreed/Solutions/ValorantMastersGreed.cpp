
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> paperRex(n);
    for (int i = 0; i < n; ++i) {
        cin >> paperRex[i];
    }

    vector<int> g2(n);
    for (int i = 0; i < n; ++i) {
        cin >> g2[i];
    }

    sort(paperRex.begin(), paperRex.end());
    sort(g2.begin(), g2.end());

    int wins = 0;
    int paperRex_idx = 0;
    int g2_idx = 0;

    while (paperRex_idx < n && g2_idx < n) {
        if (g2[g2_idx] > paperRex[paperRex_idx]) {
            wins++;
            paperRex_idx++;
            g2_idx++;
        } else {
            g2_idx++;
        }
    }

    cout << wins << endl;

    return 0;
}