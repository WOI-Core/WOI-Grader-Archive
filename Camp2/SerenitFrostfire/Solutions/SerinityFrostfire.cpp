#include<bits/stdc++.h>
using namespace std;

int main()
{
    ios_base :: sync_with_stdio(0);
    cin.tie(0);

    int T; cin >> T;


    int sum = 0;


    while(T--){


        double delta[8], n[10001];


        int N; cin >> N;


        for(int i = 0; i < N; i++){
            cin >> n[i];
        }


        map<double, double> d;


        for(int i = 0; i < N; i++){
            double dd; cin >> dd;
            d[n[i]] = dd;
        }


        for(int i = 1; i <= 4; i++){


            double meanE = 0, meanC = 0, cnt = 0;


            for(int j = 0; j < N; j++){
                for(int k = j + 1; k < N; k++){


                    double div = pow(n[j], i) - pow(n[k], i);


                    if(div == 0) continue;


                    double e = (double)(d[n[j]] - d[n[k]])/ div;
                    double c = d[n[j]] - e * pow(n[j], i);


                    meanE += e;
                    meanC += c;
                    cnt++;

                }
            }

            meanE /= cnt;
            meanC /= cnt;

            double mxDelta = -1e9;
            for(int j = 0; j < N; j++){
                // Use a small epsilon to avoid division by zero if d[n[j]] is 0
                mxDelta = max(mxDelta, abs(d[n[j]] - meanE * pow(n[j], i) - meanC) / (d[n[j]] + 1e-9));
            }


            delta[i] = mxDelta;
        }

        double mn = 1e9;
        int idx = 0; // Initialize idx
        for(int i = 1; i <= 4; i++){
            if(mn > delta[i]){
                mn = delta[i];
                idx = i;
            }
        }

        sum += idx;
    }

    cout << sum;

    return 0;
}
