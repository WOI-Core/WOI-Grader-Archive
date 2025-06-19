#include <iostream>
using namespace std;

int qs[2000001];
int qs_walk[2000001];

int main(){
    cin.tie(0) -> ios_base::sync_with_stdio(0);

    int N; cin >> N;

    qs[0] = qs_walk[0] = 0;
    for (int i = 1; i <= N; i++){
        int s; cin >> s;
        if(s >= 0){
            qs[i] = s + qs[i-1];
            qs_walk[i] = qs_walk[i-1];
        }else{
            qs[i] = qs[i-1];
            qs_walk[i] = qs_walk[i-1] - s;
        }
    }

    int Q; cin >> Q;
    while (Q--){
        int p, m; cin >> p >> m;

        int end = lower_bound(qs_walk, qs_walk+N+1, qs_walk[p]+m) - qs_walk;
        cout << qs[end-1] - qs[p-1] << "\n";
    }

    return 0;
}