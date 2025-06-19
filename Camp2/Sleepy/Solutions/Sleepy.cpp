#include<bits/stdc++.h>
using namespace std;

int main(){
    cin.tie(0) -> ios_base::sync_with_stdio(0);

    int N,M; cin >> N >> M;

    int T[N][M];
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            cin >> T[i][j];
        }
    }

    int dp[N][M];
    for(int i=0;i<M;i++){
        for(int j=0;j<N;j++){
            if(i == 0) dp[j][i] = T[j][i];
            else if(j == 0) dp[j][i] = T[j][i] + min(dp[j][i-1],dp[j+1][i-1]);
            else if(j == N-1) dp[j][i] = T[j][i] + min(dp[j][i-1],dp[j-1][i-1]);
            else dp[j][i] = T[j][i] + min(dp[j][i-1],min(dp[j-1][i-1],dp[j+1][i-1]));
        }
    }

    int mn = INT_MAX;
    for(int i=0;i<N;i++) mn = min(mn,dp[i][M-1]);
    cout << mn;

    return 0;
}