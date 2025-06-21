#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const int N=601;
const int di[]={0,0,-1,1};
const int dj[]={-1,1,0,0};
int A[N][N];
bool visited[N][N];
ll cnt;

int main(){
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

    int n,m;
    cin >> n >> m;
    for(int i=0;i<n;i++)for(int j=0;j<m;j++)cin >> A[i][j];

    for(int i=0;i<n;i++)for(int j=0;j<m;j++){
        if(A[i][j]==0||visited[i][j])continue;
        queue<pair<int,int>> q;
        q.push({i,j});
        visited[i][j]=true;
        while(!q.empty()){
            auto [ix,jx]=q.front();
            q.pop();


            for(int k=0;k<4;k++){
                int ik=ix+di[k];
                int jk=jx+dj[k];

                if(ik<0||jk<0||ik>=n||jk>=m||visited[ik][jk])continue;
                if(!A[ik][jk]){cnt++;continue;}
                q.push({ik,jk});
                visited[ik][jk]=true;
            }
        }
    }
    cout << cnt;

    return 0;
}