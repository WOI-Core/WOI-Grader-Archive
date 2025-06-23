#include <bits/stdc++.h>
using namespace std;

long long int ans;
long long solve(int i,long long l[],long long r[],int N) {
    if(i > N) return i;

    long long L = solve(l[i],l,r,N);
    long long R = solve(r[i],l,r,N);
    ans += abs(L-R);

    return 2 * max(L,R);
}

int main() {
    cin.tie(0) -> ios_base::sync_with_stdio(0);
    
    int N; cin >> N;

    long long l[N+1],r[N+1];
    for (int i=1;i<=N;i++) {
        cin >> l[i] >> r[i];
    }

    solve(1,l,r,N);
    cout << ans;

    return 0;
}