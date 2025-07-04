
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, x, k;
    cin >> n >> x >> k;

    vector<pair<int, int>> bears(n);
    for (int i = 0; i < n; ++i) {
        cin >> bears[i].first >> bears[i].second;
    }

    int kills = 0;
    int damage = 0;
    int remaining_k = k;

    while (remaining_k > 0) {
        int best_bear_index = -1;
        int max_damage_per_hit = -1;

        for (int i = 0; i < bears.size(); ++i) {
            if (bears[i].first <= x) {
                if (bears[i].second > max_damage_per_hit) {
                    max_damage_per_hit = bears[i].second;
                    best_bear_index = i;
                }
            }
        }

        if (best_bear_index != -1) {
            damage += bears[best_bear_index].second;
            kills++;
            bears.erase(bears.begin() + best_bear_index);
            remaining_k--;
        } else {
            break;
        }
    }

    cout << kills << " " << damage << endl;

    return 0;
}