#include <bits/stdc++.h>
using namespace std;

// Global variable to accumulate the total weight added.
long long ans = 0;

// Recursive function to calculate weights and balance the tree.
// i: current branch index
// l, r: arrays storing the left and right children/leaves
// N: total number of branches
long long solve(int i, long long l[], long long r[], int N) {
    // Base case: If i > N, it's a leaf node. Its weight is its value.
    if (i > N) {
        return i;
    }

    // Recursively solve for the left and right subtrees.
    long long left_weight = solve(l[i], l, r, N);
    long long right_weight = solve(r[i], l, r, N);

    // The weight needed to balance this branch is the absolute difference.
    // Add this to the total answer.
    ans += abs(left_weight - right_weight);

    // The new "effective weight" of the balanced branch is twice the heavier side.
    return 2 * max(left_weight, right_weight);
}

int main() {
    // Fast I/O
    cin.tie(0)->ios_base::sync_with_stdio(0);

    int N;
    cin >> N;

    // Use 1-based indexing for convenience, matching the problem statement.
    long long l[N + 1], r[N + 1];
    for (int i = 1; i <= N; i++) {
        cin >> l[i] >> r[i];
    }

    // Start the process from the root (branch 1).
    solve(1, l, r, N);

    // Print the final accumulated answer.
    cout << ans;

    return 0;
}
