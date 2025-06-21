#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

string ans[3];

string sumstring(string a,string b){
    string sum;
    if(a.size()<b.size())swap(a,b);
	int tod=0;
	for(int i=0;i<a.size();i++){
		int tmp=0;
		if(i<b.size())tmp=(a[i]-'0')+(b[i]-'0')+tod;
		else tmp=(a[i]-'0')+tod;
		tod=tmp/10;
		tmp%=10;
		sum+=tmp+'0';
	}
	if(tod)sum+=tod+'0';
    return sum;
}

int main() {
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

    string a,b;
    cin >> a >> b;
    int n=b.size();
    reverse(a.begin(),a.end());
    reverse(b.begin(),b.end());
    for(int i=0;i<n;i++){
        int tod=0;
        for(int k=0;k<i;k++)ans[i]+='0';
        for(int j=0;j<a.size();j++){
            int tmp;
            tmp=((a[j]-'0')*(b[i]-'0'))+tod;
            tod=tmp/10;
            tmp%=10;
            ans[i]+=tmp+'0';
        }
        if(tod)ans[i]+=tod+'0';
        if(i)ans[0]=sumstring(ans[0],ans[i]);
    }
    reverse(ans[0].begin(),ans[0].end());
    cout << ans[0];


    return 0;
}
