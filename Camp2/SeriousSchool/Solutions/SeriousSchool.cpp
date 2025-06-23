#include<bits/stdc++.h>
using namespace std;

// Defines a structure for each activity
struct activity{
    int start,end,day;
    double score;

    // Custom sort operator to prioritize activities
    // 1. Higher score per day (efficiency)
    // 2. Shorter duration if efficiency is the same
    // 3. Earlier start date if both above are the same
    bool operator < (const activity &act) const{
        if(score/day == act.score/act.day){
            if(day == act.day) return start < act.start;
            return day < act.day;
        }
        return score/day > act.score/act.day;
    }
};

// Checks if a date range is available to schedule an activity
bool is_avaliable(int start,int end,vector<bool> &avaliable){
    for(int i=start;i<=end;i++){
        if(!avaliable[i]) return false;
    }
    return true;
}

int main(){
    cin.tie(0) -> ios_base::sync_with_stdio(0);

    int score,n;
    cin >> score >> n;
    vector<activity> v;
    // Keep track of which days are booked
    vector<bool> avaliable(1001,true);

    for(int i=0;i<n;i++){
        int start,end;
        cin >> start >> end;
        double sc;
        cin >> sc;
        v.push_back({start,end,end-start+1,sc});
    }

    // Sort activities based on the greedy criteria
    sort(v.begin(),v.end());

    int i,day = 0;
    // First pass: Greedily pick the most efficient activities
    // that DO NOT push the score over 100 yet.
    for(i=0;i<n;i++){
        // Stop just before the activity that would meet the goal
        if(score + v[i].score >= 100) break;

        if(!is_avaliable(v[i].start,v[i].end,avaliable)) continue;

        // Book the activity dates
        for(int j=v[i].start;j<=v[i].end;j++) avaliable[j] = false;
        score += v[i].score;
        day += v[i].day;
    }

    int d = INT_MAX;
    bool morehund = false;
    // Second pass: From the remaining activities, find the one with the
    // SHORTEST duration that can get the score to 100.
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
