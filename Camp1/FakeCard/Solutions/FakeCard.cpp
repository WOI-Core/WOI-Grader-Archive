#include <bits/stdc++.h>
using namespace std;

int main() {
    int num_players;
    cin >> num_players;
    while (num_players < 1 || num_players > 10) {
        cin >> num_players;
    }

    vector<int> losers;
    vector<int> odd_cards;

    for (int player = 1; player <= num_players; player++) {
        int num_cards;
        cin >> num_cards;
        while (num_cards < 1 || num_cards > 52) {
            cin >> num_cards;
        }

        map<int, int> card_count;
        for (int i = 0; i < num_cards; i++) {
            int card;
            cin >> card;
            card_count[card]++;
        }

        for (auto it = card_count.begin(); it != card_count.end(); it++) {
            if (it->second % 2 == 1) {
                losers.push_back(player);
                odd_cards.push_back(it->first);
                break;
            }
        }
    }

    if (losers.size() == 1) {
        cout << odd_cards[0] << endl;
        cout << losers[0] << " loses" << endl;
    } else {
        cout << "tie" << endl;
    }

    return 0;
}
