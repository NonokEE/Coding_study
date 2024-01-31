//G5 17070 파이프 옮기기
#include <iostream>
#include <queue>
using namespace std;

int N;
int field[16][16];

enum pipe_direction { Horizontal, Vertical, Diagonal };

bool is_available(int x, int y, pipe_direction direction)
{
    switch (direction)
    {
    case Diagonal:
    case Horizontal:
        if (y+1 >= N) return false;
        if (field[x][y+1]) return false;
        if (direction == Horizontal) return true;
    case Vertical:
        if (x+1 >= N) return false;
        if (field[x+1][y]) return false;
        if (direction == Vertical) return true;
    default:
        if (field[x+1][y+1]) return false;
        return true;
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    // 입력
    scanf("%d",&N);

    for(int i = 0 ; i < N ; i++)
    {
        for(int j = 0 ; j < N ; j++)
        {
            scanf("%d",&field[i][j]);
        }
    }

    // 초기화
    int res = 0;
    queue<pair<pair<int,int>, pipe_direction>> q;
    q.push(make_pair(make_pair(0,1), Horizontal));

    // 루프 진행
    while(! q.empty())
    {
        int cx = q.front().first.first;
        int cy = q.front().first.second;
        pipe_direction cd = q.front().second;
        q.pop();

        // 도착한 경우
        if (cx == N-1 && cy == N-1)
        {
            res++;
            continue;
        }

        // 이동
        switch (cd)
        {
        case Horizontal:
            if (is_available(cx, cy, Horizontal)) q.push(make_pair(make_pair(cx, cy+1), Horizontal));
            if (is_available(cx, cy, Diagonal)) q.push(make_pair(make_pair(cx+1, cy+1), Diagonal));
            break;
        case Vertical:
            if (is_available(cx, cy, Vertical)) q.push(make_pair(make_pair(cx+1, cy), Vertical));
            if (is_available(cx, cy, Diagonal)) q.push(make_pair(make_pair(cx+1, cy+1), Diagonal));
            break;
        case Diagonal:
            if (is_available(cx, cy, Horizontal)) q.push(make_pair(make_pair(cx, cy+1), Horizontal));
            if (is_available(cx, cy, Vertical)) q.push(make_pair(make_pair(cx+1, cy), Vertical));
            if (is_available(cx, cy, Diagonal)) q.push(make_pair(make_pair(cx+1, cy+1), Diagonal));
            break;
        }
    }
    
    // 출력
    printf("%d", res);
}
