#include<bits/stdc++.h>

using namespace std;

int arr[10] , n , m , cnt , p , h ;
bool visited[10] ;

struct condition {
    int pos , have ;
    condition(){}
};

condition conditions [10] ;
int number_conditions [10][10] ;

void solve(int idx){

    if(idx == n){

        for(int i = 0 ; i < m ; i ++ ){
            
            //check pos
            int cnt_pos = 0 , cnt_have = 0 ;

            for(int j = 0 ; j < n ; j ++ ){

                if (arr[j] == number_conditions[i][j]){
                    cnt_pos ++ ;
                }

            } 
            //check have
            for(int j = 0 ; j < n ; j ++ ){

                for(int k = 0 ; k < n ; k ++ ){

                    if(j != k && arr[j] == number_conditions[i][k]){
                        cnt_have ++ ;
                    }

                }

            }

            if(conditions[i].have != cnt_have || conditions[i].pos != cnt_pos){
                return ;
            }
        }

        cnt ++ ;

        for(int i = 0 ; i < n ; i ++ ){
            cout << arr[i] << ' ' ;
        }
        cout << '\n' ;

        return ;
    }
    else {

        for(int i = 1 ; i <= 9 ; i ++ ){

            if(!visited[i]){

                visited[i] = true ;
                arr[idx] = i ;

                solve(idx + 1) ;

                visited[i] = false ;
                arr[idx] = 0 ;

            }
        }
        return ;
    }
    return ;
}

int main(){

    ios_base :: sync_with_stdio(0) , cin.tie(0) ;

    cin >> n >> m ;

    for(int i = 0 ; i < m ; i ++ ){

        for(int j = 0 ; j < n ; j ++ ){
            cin >> number_conditions[i][j] ;
        }

        cin >> p >> h ;

        conditions[i].pos = p ;
        conditions[i].have = h ;

    }

    solve(0) ;

    cout << cnt ;

    return 0 ;
}
