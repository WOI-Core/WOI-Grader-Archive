#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
int main() {
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

    vector<int> A;
    int n,w,temp;
    cin >> n >> w;
    for(int i=0;i<n;i++){
        cin >> temp;
        A.push_back(temp);
    }
    sort(A.begin(),A.end());
    int l=0,r=n-1,cnt=0;
    while(l<=r){
        if(A[l]+A[r]<=w){
            cnt++;
            l++;
            r--;
        }else{
            r--;
            cnt++;
        }
    }
    cout << cnt;
    
    return 0;
}