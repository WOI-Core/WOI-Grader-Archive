#include<bits/stdc++.h>
using namespace std;

int dx[] = {-2,-2,-1,-1,1,1,2,2};
int dy[] = {-1,1,-2,2,-2,2,-1,1};

bool is_valid(int i,int j,int N){
    if(i < 0 || j < 0 || i >= N || j >= N) return false;
    return true;
}

int solve(int N,int a,int b,int c,int d){
    bool visited[N][N];
    memset(visited,false,sizeof(visited));

    queue<pair<int,int>> q;
    q.push({a,b});
    visited[a][b] = true;

    int step = 0;
    while(!q.empty()){
        int size = q.size();

        step ++;
        while(size--){
            int x = q.front().first;
            int y = q.front().second;

            q.pop();
            for(int k=0;k<8;k++){
                int i = x+dx[k];
                int j = y+dy[k];
                if(i == c && j == d) return step;
                if(is_valid(i,j,N) && !visited[i][j]){
                    q.push({i,j});
                    visited[i][j] = true;
                }
            }
        }
    }

    return -1;
}

int main(){
    cin.tie(0) -> ios_base::sync_with_stdio(0);

    int N; cin >> N;
    int c,d; cin >> c >> d;
    int a,b; cin >> a >> b;

    cout << solve(N,a-1,b-1,c-1,d-1);

    return 0;
}