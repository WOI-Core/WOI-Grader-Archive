#include<bits/stdc++.h>

using namespace std;

int N , T , x , y , point_a = 0 , point_b = 0 , init_power_a , init_power_b ;
char cmd ;
deque<int> a , b ;

void display(){
    
    for(int i = 0 ; i < 3 ; i ++ ){
        cout << a[i] << ' ' ;
    }
    cout << '\n' ;

    for(int i = 0 ; i < 3 ; i ++ ){
        cout << b[i] << ' ' ;
    }
    cout << '\n' ;

}

int main(){

    ios_base :: sync_with_stdio(0) , cin.tie(0);

    cin >> N >> T ;

    for(int i = 0 ; i < N ; i ++ ){
        cin >> x ;
        a.push_back(x) ;
    }

    for(int i = 0 ; i < N ; i ++ ){
        cin >> y ;
        b.push_back(y) ;
    }

    init_power_a = a[0] ;
    init_power_b = b[0] ;

    while (T -- ){
        
        cin >> cmd ;

        if(cmd == 'A'){

            if(a[0] > b[0]){
                point_a ++ ;
                a[0] -= b[0] ;
                b.pop_front() ;
                b.push_back(init_power_b) ;
                init_power_b = b[0] ;
            }
            else if(b[0] > a[0]){
                point_b ++ ;
                b[0] -= a[0] ;
                a.pop_front() ;
                a.push_back(init_power_a) ;
                init_power_a = a[0] ;
            }
            else {
                point_a ++ ;
                point_b ++ ;
                
                a.pop_front() ;
                b.pop_front() ;

                a.push_back(init_power_a) ;
                b.push_back(init_power_b) ;

                init_power_a = a[0] ;
                init_power_b = b[0] ;
            }
        }
        else {
            display() ;
        }
    }
    cout << point_a << ' ' << point_b ;

    return 0 ;
}