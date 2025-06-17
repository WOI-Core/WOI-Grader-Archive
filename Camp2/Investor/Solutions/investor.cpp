#include<iostream>

using namespace std;

const int SIZE = 2e5 + 1 ;

int N , Q ;
int parentLeft [SIZE] , parentRight [SIZE] ;
long long initValue [SIZE] , currentValue[SIZE] ;
char cmd ;

void init(){

    for(int i = 0 ; i < SIZE ; i++){
        parentLeft[i] = i ;
        parentRight[i] = i ;
    }

    return ;
}

int findParentLeft(int node){

    if(parentLeft[node] == node) return node ;
    else return parentLeft[node] = findParentLeft(parentLeft[node]) ;
    
}

int findParentRight(int node){

    if(parentRight[node] == node) return node ;
    else return parentRight[node] = findParentRight(parentRight[node]) ;
    
}

void setCurrentValue(int mainRoot  , int subRoot){

    currentValue[mainRoot] += currentValue[subRoot] ;
    currentValue[subRoot] = 0 ;

    return ;
}

void setCurrentValueByInitValue(int mainRoot , int x , int y){

    currentValue[mainRoot] += initValue[x] + initValue[y] ;

    return ;
}

void merge(int x , int y){

    if(x > y) swap(x, y) ;

    int rootLeftX = findParentLeft(x) ;
    int rootLeftY = findParentLeft(y) ;

    int mainRoot , subRoot ;

    //merge left root 
    if(rootLeftX == rootLeftY) {

        mainRoot = rootLeftX ;
        setCurrentValueByInitValue(mainRoot , x , y) ;

    }
    else if(rootLeftX < rootLeftY){

        parentLeft[rootLeftY] = rootLeftX ;

        mainRoot = rootLeftX ;
        subRoot = rootLeftY ;

        setCurrentValue(mainRoot , subRoot) ;
    }
    else {
        parentLeft[rootLeftX] = rootLeftY ;

        mainRoot = rootLeftY ;
        subRoot = rootLeftX ;

        setCurrentValue(mainRoot , subRoot) ;
    }

    //merge right root 

    int rootRightX = findParentRight(x) ;
    int rootRightY = findParentRight(y) ;


    if(rootRightX == rootRightY) {

        return ;

    }
    else if(rootRightY < rootRightX){

        parentRight[rootRightY] = rootRightX ;

    }
    else {
        parentRight[rootRightX] = rootRightY ;

    }

    return ;
}

int queryRange(int node){

    int rootLeftNode = findParentLeft(node) , rootRightNode = findParentRight(node) ;
    return rootRightNode - rootLeftNode + 1 ;

}

long long queryValue(int node){

    int root = findParentLeft(node) ;
    return currentValue[root] ;

}

int main(){

    ios_base :: sync_with_stdio(0) , cin.tie(0) ;

    init(); 

    cin >> N >> Q ;

    for(int i = 1 ; i <= N ; i ++ ){
        cin >> initValue[i] ;
        currentValue[i] = initValue[i] ;
    }

    while(Q -- ){

        cin >> cmd ;

        //command A merge x , y ;
        if(cmd == 'A'){

            int x , y ; cin >> x >> y ;
            merge(x , y) ;

        }
        //command B display range 
        if(cmd == 'B'){

            int node ; cin >> node ;
            int range = queryRange(node) ;

            cout << range << '\n' ;

        }
        //command C display current value
        if(cmd == 'C'){

            int node ; cin >> node ;
            long long value = queryValue(node) ;

            cout << value << '\n' ;
        }
        //command D display range and value 
        if(cmd == 'D'){

            int node ; cin >> node ;
            int range = queryRange(node) ;
            long long value = queryValue(node) ;

            cout << range << ' ' << value << '\n' ;
        }

    }

    return 0 ;
}