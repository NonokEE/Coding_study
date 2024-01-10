//G5 1351 무한 수열
#include <iostream>
#include <map>
using namespace std;

long long n, p, q;
map<long long,long long> dict;

long long recursion(long long val)
{
    if (dict.find(val) != dict.end())
    {
        return dict[val];
    }
    else
    {
        dict.insert(pair<long long,long long>(val, recursion(val/p) + recursion(val/q)));
        return dict[val];
    }
}

int main()
{
    scanf("%lld %lld %lld", &n, &p, &q);

    dict.insert(pair<long long,long long>(0,1));

    printf("%lld", recursion(n));
}
