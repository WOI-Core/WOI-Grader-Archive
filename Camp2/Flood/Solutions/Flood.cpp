#include <bits/stdc++.h>

using namespace std;
int main() {
    int i;
    int n;
    double p, h = 0;
    cin >> n >> p;
    int r[n], rc[n];
    for (i = 0; i < n; i++) {
        cin >> r[i];
        rc[i] = r[i];
    }
    sort(r, r + n);
    for (i = 0; i < n; i++) {
        if (p > (r[i] - h)*(n - i)) {
            p -= (r[i] - h)*(n - i);
            h = r[i];
        }
        else {
            h += p/(n - i);
            break;
        }
    }
    for (i = 0; i < n; i++) {
        if (h >= rc[i]) {
            cout << rc[i];
        }
        else {
            if (h == floor(h)) {
                cout << (int) h;
            }
            else {
                cout << fixed << setprecision(2) << h;
            }
        }
        cout << "\n";
    }
    return 0;
}