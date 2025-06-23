#include <iostream>
#include <algorithm>

using namespace std;

// Using vectors for dynamic sizing, although constraints are large
// The provided solution uses static arrays which is also fine
long long qs[2000001];
long long qs_walk[2000001];

int main(){
    cin.tie(0)->sync_with_stdio(0);

    int N;
    cin >> N;

    // Initialize prefix sums at index 0
    qs[0] = 0;
    qs_walk[0] = 0;

    // Build prefix sum arrays
    for (int i = 1; i <= N; i++){
        int s;
        cin >> s;
        if(s >= 0){
            // Add to sandwich sum, no cost
            qs[i] = s + qs[i-1];
            qs_walk[i] = qs_walk[i-1];
        } else {
            // No sandwich, add to endurance cost
            qs[i] = qs[i-1];
            qs_walk[i] = qs_walk[i-1] - s; // cost is positive
        }
    }

    int Q;
    cin >> Q;
    while (Q--){
        int p;
        long long m;
        cin >> p >> m;

        // Find the total endurance cost we can afford from the start
        long long target_cost = qs_walk[p-1] + m;

        // Find the first position where the accumulated cost exceeds our target cost
        // The result is an iterator, subtracting the beginning gives the index.
        int end_idx = upper_bound(qs_walk, qs_walk + N + 1, target_cost) - qs_walk;

        // The total sandwiches collected is the sum up to the position *before* the end
        cout << qs[end_idx - 1] - qs[p-1] << "\n";
    }

    return 0;
}
