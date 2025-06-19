#include <iostream>
// #include "inout.h"
using namespace std;

const int m = 1e9+7;
int fw[1000005];

void upd (int i, int v = 1) { for (; i <= 1e6+1; i+=i&-i) fw[i]+=v; }
int qry (int i) {
    int s = 0;
    for (; i; i-=i&-i) s += fw[i];
    return s;
}

int main () {
    ios_base::sync_with_stdio(0);
    cout.tie(0);
    cin.tie(0);

    // inout();

    int n, a; cin >> n;
    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a;
        ans = (ans+qry(1e6-a+1))%m;
        upd(1e6-a+1);
    }
    cout << ans;
}