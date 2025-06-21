#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
const int N=1001,M=1e9+7;
ll dp[N][5001],A[N],n,k;

ll solve(int i,ll sum){
    if(i==n)return sum==k;
    if(dp[i][sum]!=-1)return dp[i][sum];
    return dp[i][sum]=(solve(i+1,sum+A[i])+solve(i+1,sum-A[i]))%M;
}

int main(){
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

    cin >> n >> k;
    memset(dp,-1,sizeof(dp));
    for(int i=0;i<n;i++)cin >> A[i];
    cout << solve(0,0);

    return 0;
}