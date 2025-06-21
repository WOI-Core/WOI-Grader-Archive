#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int n,mx=-1,A[11][11],c[11],dia[11][11];
int di[]={-2,-1,1,2};
int dj[]={1,2,2,1};

void sSearch(int r,int sum){
    if(r==n)mx=max(mx,sum);
    else{
        for(int i=0;i<n;i++){
            if(c[i]||dia[r][i])continue;

            c[i]=1;
            for(int k=0;k<4;k++){
                int dr=r+dj[k];
                int dc=i+di[k];
                if(dr<0||dr>=n||dc>=n)continue;
                dia[dr][dc]=1;
            }

            sSearch(r+1,sum+A[r][i]);

            c[i]=0;
            for(int k=0;k<4;k++){
                int dr=r+dj[k];
                int dc=i+di[k];
                if(dr<0||dr>=n||dc>=n)continue;
                dia[dr][dc]=0;
            }
        }
    }
}

int main(){
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

    cin >> n;
    for(int i=0;i<n;i++)for(int j=0;j<n;j++)cin >> A[i][j];
    sSearch(0,0);
    cout << mx;

    return 0;
}