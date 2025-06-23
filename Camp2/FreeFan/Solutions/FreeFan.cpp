#include <bits/stdc++.h> 
using namespace std;
vector<string> moves;
void hanoi_solver(int n, int source_peg, int target_peg, int auxiliary_peg) {
    if (n == 0) {
        return;
    }
    hanoi_solver(n - 1, source_peg, auxiliary_peg, target_peg);
    moves.push_back(to_string(n) + " " + to_string(source_peg) + " " + to_string(target_peg));
    hanoi_solver(n - 1, auxiliary_peg, target_peg, source_peg);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N;
    cin >> N; 
    hanoi_solver(N, 1, 3, 2);
    cout << moves.size() << endl;
    for (const string& move : moves) {
        cout << move << endl; 
    }

    return 0;
}