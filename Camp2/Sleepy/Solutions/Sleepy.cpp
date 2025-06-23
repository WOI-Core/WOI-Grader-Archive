#include<bits/stdc++.h>
using namespace std;

int main(){
    cin.tie(0) -> ios_base::sync_with_stdio(0);

    int N,M;
    cin >> N >> M;

    // Using a vector of vectors for dynamic 2D array
    vector<vector<int>> T(N, vector<int>(M));
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            cin >> T[i][j];
        }
    }

    vector<vector<int>> dp(N, vector<int>(M));

    // Iterate column by column
    for(int j=0; j<M; j++){
        // Iterate row by row
        for(int i=0; i<N; i++){
            if(j == 0) {
                // Base case: For the first column, cost is just the cell's time
                dp[i][j] = T[i][j];
            } else {
                // Find the minimum cost from the 3 possible previous cells
                int prev_min = dp[i][j-1]; // From the middle
                if (i > 0) {
                    prev_min = min(prev_min, dp[i-1][j-1]); // From top-left
                }
                if (i < N - 1) {
                    prev_min = min(prev_min, dp[i+1][j-1]); // From bottom-left
                }
                dp[i][j] = T[i][j] + prev_min;
            }
        }
    }

    // The answer is the minimum cost in the last column
    int mn = INT_MAX;
    for(int i=0; i<N; i++) {
        mn = min(mn, dp[i][M-1]);
    }
    cout << mn;

    return 0;
}
