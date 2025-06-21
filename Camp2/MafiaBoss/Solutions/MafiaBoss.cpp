#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
vector<int> adj[(int)2e5+10];
int color[(int)2e5+10];
int n,e;
int main(){
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

    cin >> n >> e;
    for(int i=0;i<e;i++){
        int a,b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    int mx=-1;
    for(int k=1;k<n+1;k++){
        for(int i=1;i<n+1;i++){
            for(auto child:adj[i]){
                if(color[child]==color[i])color[child]++;
                mx=max(mx,color[child]);
            }
        }
    }
    cout << mx+1;

    return 0;
}