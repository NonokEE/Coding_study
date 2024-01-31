//G4 12851 숨바꼭질 2
#include <iostream>
using namespace std;
//
#define MAX 9999999
#include <queue>
int N, K;
int field[100001];

int res_sec = MAX;
int res_count = 0;
//
bool is_infield(int num) { return (0 <= num) && (num <= 100000); }

//
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    //
    cin >> N >> K;
    if (N==K)
    {
        cout << 0 << endl << 1;
        return 0;
    }

    for(int i = 0 ; i < 100001 ; i++) field[i] = MAX;
    
    field[N] = 0;
    queue<pair<int,int>> q;   //시간, 위치
    q.push(make_pair(0,N));

    while(! q.empty())
    {
        int step = q.front().first;
        int loc = q.front().second;

        //중단 조건 확인
        if ((loc+1 == K) || (loc-1 == K) || (loc*2 == K))
        {
            res_sec = step+1;
            break;
        }

        q.pop();
        //이동
        if(is_infield(loc+1) && (field[loc+1] >= step + 1)) 
        {
            q.push(make_pair(step+1, loc+1));
            field[loc+1] = step+1;
        }
        if(is_infield(loc-1) && (field[loc-1] >= step + 1)) 
        {
            q.push(make_pair(step+1, loc-1));
            field[loc-1] = step+1;
        }
        if(is_infield(loc*2) && (field[loc*2] >= step + 1)) 
        {
            q.push(make_pair(step+1, loc*2));
            field[loc*2] = step+1;
        }
    }

    while((!q.empty()) && (q.front().first == res_sec-1))
    {
        int loc = q.front().second;
        q.pop();

        if(is_infield(loc+1) && (loc+1 == K)) res_count += 1;
        if(is_infield(loc-1) && (loc-1 == K)) res_count += 1;
        if(is_infield(loc*2) && (loc*2 == K)) res_count += 1;
    }

    cout << res_sec << endl << res_count;

    return 0;
}
