#include<bits/stdc++.h>
using namespace std;

struct activity{
    int start,end,day;
    double score;

    bool operator < (const activity &act) const{
        if(score/day == act.score/act.day){
            if(day == act.day) return start < act.start;
            return day < act.day;
        }
        return score/day > act.score/act.day;
    }
};

bool is_avaliable(int start,int end,vector<bool> avaliable){
    for(int i=start;i<=end;i++){
        if(!avaliable[i]) return false;
    }
    return true;
}

int main(){
    cin.tie(0) -> ios_base::sync_with_stdio(0);

    int score,n; cin >> score >> n;
    vector<activity> v;
    vector<bool> avaliable(1001,true);
    
    for(int i=0;i<n;i++){
        int start,end; cin >> start >> end;
        double sc; cin >> sc;
        v.push_back({start,end,end-start+1,sc});
    }
    sort(v.begin(),v.end());
    // cout << "\n";
    // for(auto x : v){
    //     cout << x.start << "\t" << x.end << "\t" << x.day << "\t" << x.score << "\t-> " << x.score/x.day << "\n";
    // }
    // cout << "\n";

    int i,day = 0;
    for(i=0;i<n;i++){
        if(score + v[i].score >= 100) break;

        if(!is_avaliable(v[i].start,v[i].end,avaliable)) continue;

        for(int j=v[i].start;j<=v[i].end;j++) avaliable[j] = false;
        score += v[i].score;
        day += v[i].day;
    }

    int d = INT_MAX;
    bool morehund = false;
    for(int j=i;j<n;j++){
        if(is_avaliable(v[j].start,v[j].end,avaliable) && score + v[j].score >= 100){
            d = min(d,v[j].day);
            morehund = true;
        }
    }

    if(!morehund) cout << -1;
    else cout << day + d;

    return 0;
}