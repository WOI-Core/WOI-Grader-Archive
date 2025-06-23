//Task : LablaeCave


#include <bits/stdc++.h>
using namespace std;


int dp(int row, int col1, int col2,vector<vector<int> >& val,vector<vector<vector<int> > >& vis)
{
    if (col1 < 0  ||col1 >= val[0].size()|| col2 < 0 || col2 >= val[0].size()){
        return 0;
    }

    if (vis[row][col1][col2] != -1){
        return vis[row][col1][col2];
    }

    int ans = val[row][col1];


    if (col1 != col2){
        ans += val[row][col2];
    }
    if (row != val.size() - 1) {
        int mx = 0;

        for (int ncol1 = col1 - 1;ncol1 <= col1 + 1; ncol1++){

            for (int ncol2 = col2 - 1;ncol2 <= col2 + 1;ncol2++){
                mx = max(mx,dp(row + 1, ncol1,ncol2, val,vis)); 
            }

        }
        ans += mx;
    }

    vis[row][col1][col2] = ans;

    return ans;
}
 
int selected(vector<vector<int> >& val)
{
    int N = val.size();

    if (N == 0){
        return 0;
    }
    int M = val[0].size();

    if (M == 0){
        return 0;
    }
    vector<vector<vector<int> > >vis(N, vector<vector<int> >(M, vector<int>(M, -1)));

    return dp(0, 0, M - 1, val, vis);
}
 
int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);

    int N,M;cin>>N>>M;
    vector<vector<int> > val(N,vector<int>(M));
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            cin>>val[i][j];
        }
    }
    cout << selected(val) ;
    return 0;
}