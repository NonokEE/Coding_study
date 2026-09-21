//G4 11054 가장 긴 바이토닉 부분 수열
#include <iostream>
using namespace std;
//
int N;
int A[1000];
int increasing[1000];
int decreasing[1000];

int res = 0;
//
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    //
    cin >> N;
    for(int i = 0 ; i < N ; i++) cin >> A[i];

    increasing[0] = 1;
    for(int i = 0 ; i < N ; i++)
    {
        increasing[i] = 1;
        for(int j = 0 ; j < i ; j++)
        {
            if(A[i] > A[j]) increasing[i] = max(increasing[i], increasing[j] + 1);
        }
    }

    for(int i = N-1 ; i >= 0 ; i--)
    {
        decreasing[i] = 1;
        for(int j = N-1 ; j > i ; j--)
        {
            if(A[i] > A[j]) decreasing[i] = max(decreasing[i], decreasing[j] + 1);
        }
    }

    for(int i = 0 ; i < N ; i++) res = max(res, increasing[i] + decreasing[i]);

    cout << res-1;
}
