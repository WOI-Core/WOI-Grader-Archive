#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main(){
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

    // Number of queries
    ll q;
    cin >> q;

    while(q--){
        // M: target number of houses to burn
        ll n;
        cin >> n;

        // Binary search for the number of bottles (k)
        // The search space for k is from 0 to n, as k > n is never optimal.
        unsigned long long l=0, r=n, mid;
        while(l<r){
            mid=(l+r)/2;

            // Calculate total houses burned for 'mid' bottles
            // The logic is that k bottles burn k houses, and for every 10 burned,
            // you get a bonus. The C++ code models this as:
            // total_burned = k + k/10 + k/100 + k/1000 + ...
            ll sum=0, tmp=mid;
            while(tmp > 0){
                sum += tmp/10;
                tmp /= 10;
            }

            if(mid + sum < n) {
                // Not enough houses burned, need more bottles
                l = mid + 1;
            } else {
                // Enough houses burned, try with fewer bottles
                r = mid;
            }
        }
        // 'l' is the smallest number of bottles that meets the requirement
        cout << l << " ";
    }

    return 0;
}
