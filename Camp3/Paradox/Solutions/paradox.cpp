#include<bits/stdc++.h>

using namespace std ;

const int N = 100001 ;
const int INF = 1000001 ;

struct coor {
    int x , y , type , idx ;
    bool operator <  (const coor & rhs)const { 
        if(x != rhs.x)return x < rhs.x ;
        return y < rhs.y ;
    }
};

class Segment {

    public : 

        int seg[4 * N] ;

        void init(){

            for(int i = 0 ; i < 4 * N ; i ++ ){
                seg[i] = INF ; 
            }

        }

        void update(int l , int r , int idx , int val , int now){

            if(l > idx || r < idx)return ;

            if(l == r){
                seg[now] = min(seg[now] , val) ;
                return ;
            }

            int mid = (l + r) >> 1 ;

            update(l , mid , idx , val , now * 2) ;
            update(mid + 1 , r , idx , val , now * 2 + 1) ;

            seg[now] = min(seg[now * 2] , seg[now * 2 + 1]) ;
        }

        int query(int l , int r , int curr_l , int curr_r , int now){

            if(curr_l > r || curr_r < l)return INF ;
            if(l <= curr_l && curr_r <= r)return seg[now] ;

            int mid = (curr_l + curr_r) >> 1 ;
            return min(query(l , r , curr_l , mid , now * 2) , query(l , r , mid + 1 , curr_r , now * 2 + 1)) ;
        }
}seg[2] ;

int n , m ;

coor time_holes [2 * N] ;

int dis[2][N] , ans[N] ;

int main(){

    ios_base :: sync_with_stdio(0) , cin.tie(0) ;

    cin >> n >> m ;

    for(int i = 0 ;  i < n ; i ++ ){
        cin >> time_holes[i].x >> time_holes[i].y ;
        time_holes[i].type = 0 ;
        time_holes[i].idx = 0 ;
    }

    for(int i = 0 ;  i < m ; i ++ ){
        cin >> time_holes[n + i].x >> time_holes[n + i].y ;
        time_holes[n + i].type = 1 ;
        time_holes[n + i].idx = i + 1 ;
    }


    sort(time_holes , time_holes + n + m) ;

    seg[0].init() ;
    seg[1].init() ;

    for(int i = 0 ; i < n + m ; i ++ ){

        int x = time_holes[i].x , y = time_holes[i].y , type = time_holes[i].type , idx = time_holes[i].idx ;

        if(type == 1){

            int left = seg[0].query(1 , y , 1 , N , 1) + x + y ;
            int right = seg[1].query(y , N , 1 , N , 1) + x - y ;
            dis[0][idx] = min(left , right) ;

        }
        
        if(type == 0){
            seg[0].update(1 , N , y , - x - y , 1) ;
            seg[1].update(1 , N , y , - x + y , 1) ;
        }
        
    }

    seg[0].init() ;
    seg[1].init() ;

    for(int i = n + m - 1 ; i >= 0 ; i -- ){

        int x = time_holes[i].x , y = time_holes[i].y , type = time_holes[i].type , idx = time_holes[i].idx ;

        if(type == 1){
            int left = seg[0].query(1 , y , 1 , N , 1) - x + y ;
            int right = seg[1].query(y , N , 1 , N , 1) - x - y ;
            dis[1][idx] = min(left , right) ;
        }
        
        if(type == 0){
            seg[0].update(1 , N , y , x - y , 1) ;
            seg[1].update(1 , N , y , x + y , 1) ;
        }
        
    }

    for(int i = 1 ; i <= m ; i ++ ){
        cout << min(dis[0][i] , dis[1][i]) << '\n' ;
    }
   
    
    return 0 ;
}