//G5 1107 리모컨
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int N, M;
    cin >> N >> M;

    bool broken[10];
    for(int i = 0 ; i < 10 ; i++) broken[i] = false;

    for(int i = 0 ; i < M ; i++)
    {
        int input;
        cin >> input;
        broken[input] = true;
    }

    //

    int res = abs(N - 100);

    for (int ch = 0 ; ch < 1000001; ch++)
    {
        string str_ch = to_string(ch);
        bool flag = true;
        for (string::iterator digit = str_ch.begin() ; digit != str_ch.end() ; ++ digit)
        {
            if(broken[(*digit) - '0']) 
            {
                flag = false;
                break;
            }

        }
        if (flag)
        {
            int temp = to_string(ch).length() + abs(ch - N);
            res = min(res, temp);
        }
    }
    cout << res;
}
