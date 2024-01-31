//G4 13172 시그마
#include <iostream>
using namespace std;
//
#define CAP 1000000007
#define BIG long long

BIG m;
BIG res = 0;

//
BIG power(BIG n, BIG p)
{
    BIG res = 1;
    while(p)
    {
        if(p%2) res = res * n % CAP;
        p /= 2;
        n = n * n % CAP;
    }
    return res;
}

//
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    // 
    cin >> m;
    for(int i = 0 ; i < m ; i++)
    {
        BIG denominator, numerator;
        cin >> denominator >> numerator;

        res += (numerator * (power(denominator, CAP - 2))) % CAP;
    }
    cout << res % CAP;
}
