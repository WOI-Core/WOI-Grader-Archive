#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
int main(){
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

    vector<ll> price,product;
    unordered_map<string,ll> mp;

    ll n,m,tmp;
    cin >> n >> m;
    for(int i=0;i<n;i++){cin >> tmp;price.push_back(tmp);}

    string s;
    for(int i=0;i<m;i++){cin >> s;mp[s]++;}

    for(auto i:mp)product.push_back(i.second);

    sort(price.begin(),price.end());
    sort(product.begin(),product.end(),greater<int>());

    ll sum=0;
    for(int i=0;i<m;i++)sum+=price[i]*product[i];
    cout << sum << " ";

    sum=0;
    reverse(price.begin(),price.end());
    for(int i=0;i<m;i++)sum+=price[i]*product[i];
    cout << sum;

    return 0;
}