
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> prices(n);
    for (int i = 0; i < n; ++i) {
        cin >> prices[i];
    }

    sort(prices.begin(), prices.end());

    long long total_price = 0;
    for (int price : prices) {
        total_price += price;
    }

    cout << total_price << endl;

    return 0;
}