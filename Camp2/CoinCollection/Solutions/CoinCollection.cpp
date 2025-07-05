
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> coins(n);
    for (int i = 0; i < n; ++i) {
        cin >> coins[i];
    }

    sort(coins.rbegin(), coins.rend());

    int total_value = 0;
    for (int coin : coins) {
        total_value += coin;
    }

    int player_value = 0;
    int moves = 0;
    for (int i = 0; i < n; ++i) {
        player_value += coins[i];
        moves++;
        if (player_value > total_value - player_value) {
            break;
        }
    }

    cout << moves << endl;

    return 0;
}