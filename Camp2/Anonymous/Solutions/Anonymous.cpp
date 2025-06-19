#include <bits/stdc++.h>
using namespace std;
#define ll long long

const int mxN = 2e8+1;
const int mxA = 12e6;

bitset<mxN> isNotPrime;

int prime[mxA], cnt;

int main() {

    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

    prime[cnt++] = 2;
    for(ll i=3; i<mxN; i+=2) {
        if(isNotPrime[i]) continue;
        prime[cnt++] = i;
        for(ll j=i*i; j<mxN; j+=i<<1) isNotPrime[j] = 1;
    }
    int Q; 
    cin >> Q;
    while(Q--) {
        int n; 
        cin >> n;
        auto it = upper_bound(prime, prime + cnt, n) - 1;
        if(*it==n) cout << it-prime+1 << "\n"; else cout << *it << "\n";
    }
    return 0;
}