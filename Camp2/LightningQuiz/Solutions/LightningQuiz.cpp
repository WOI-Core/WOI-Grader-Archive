#include <bits/stdc++.h>
using namespace std;
#define ll long long

// 15,485,863 is the 1,000,000th prime number then possible mxN is 20,000,000
// As you can see in the example that what is 1,000,000th prime number

const int mxN = 2e7;
const int mxK = 1e6+10;
const int MOD = 1e9+7;

bool isNotPrime[mxN];
vector<int> prime;

void getPrime() {
    for(int i=2; prime.size() < mxK; i++) {
        if(isNotPrime[i]) continue;
        prime.push_back(i);
        for(int j=2; j*i<mxN; j++) isNotPrime[i*j] = true;
    }
}

int main() {
    getPrime();
    int a, b;
    cin >> a >> b;
    int sum = 0;
    for(int i=a; i<=b; i++) {
        sum += prime[i-1];
        sum%=MOD;
    }
    cout << sum%MOD;
    return 0;
}