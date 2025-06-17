#include<bits/stdc++.h>

using namespace std;

class Fenwick {

    public :
        int fw[100002] ;

        void update(int idx , int val){
            for(; idx < 100002; idx += (idx & -idx)){
                fw[idx] += val ;
            }
        }

        int query(int idx){
            int res = 0 ;
            for(; idx > 0 ; idx -= (idx & -idx)){
                res += fw[idx] ;
            }
            return res ;
        }
}fw;

int main(){

    ios_base :: sync_with_stdio(0) , cin.tie(0);

    int n , q , a , b , d , x , c ;
    
    cin >> n >> q >> a >> b ;

    while(q -- ){
        cin >> d >> x >> c ;
        if(d == 1){
            fw.update(1 , c) ;
            fw.update(x + 1 , -c) ;

            int l = 1 , r = n , ans_l , ans_r ;

            while(l < r){
                int mid = (l + r) >> 1 ;
                if(fw.query(mid) <= b)r = mid ;
                else l = mid + 1 ;
            }

            ans_l = l ;

            l = 1 , r = n ;

            while(l < r){
                int mid = (l + r + 1) >> 1 ;
                if(fw.query(mid) >= a)l = mid ;
                else r = mid - 1 ;
            }

            ans_r = r ;

            if(ans_l < ans_r){
                cout << ans_l << ' ' << ans_r << '\n' ;
            }
            else if(ans_l == ans_r && fw.query(ans_l) >= a && fw.query(ans_r) <= b){
                cout << ans_l << '\n' ;
            }
            else {
                cout << -1 ;
            }

        }
        if(d == 2){
            fw.update(x , -c) ;

            int l = 1 , r = n , ans_l , ans_r ;

            while(l < r){
                int mid = (l + r) >> 1 ;
                if(fw.query(mid) <= b)r = mid ;
                else l = mid + 1 ;
            }

            ans_l = l ;

            l = 1 , r = n ;

            while(l < r){
                int mid = (l + r + 1) >> 1 ;
                if(fw.query(mid) >= a)l = mid ;
                else r = mid - 1 ;
            }

            ans_r = r ;

            if(ans_l < ans_r){
                cout << ans_l << ' ' << ans_r << '\n' ;
            }
            else if(ans_l == ans_r && fw.query(ans_l) >= a && fw.query(ans_r) <= b){
                cout << ans_l << '\n' ;
            }
            else {
                cout << -1 ;
            }
        }
    }
    return 0 ;
}
