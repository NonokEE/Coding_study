//S1 2178 미로 탐색
#include <iostream>
#include <queue>

using namespace std;

#define INF 10000
#define MAX_VAL 101

int main()
{
    int N, M;
    cin >> N >> M;

    int field[MAX_VAL][MAX_VAL];

    for(int x = 0 ; x < N ; x++)
    {
        string line;
        cin >> line;

        for(int y = 0 ; y < M ; y++)
        {
            field[x][y] = line[y] - '0';
        }
    }

    //

    int dx[] = {-1,1,0,0};
    int dy[] = {0,0,-1,1};

    queue<pair<int,int>> q;
    q.push(make_pair(0,0));

    while (! q.empty())
    {
        int cx = q.front().first;
        int cy = q.front().second;
        q.pop();

        if (cx == N-1 && cy == M-1) break;

        for(int dir = 0 ; dir < 4 ; dir++)
        {
            int nx = cx + dx[dir];
            int ny = cy + dy[dir];

            if (! ((0 <= nx && nx < N) && (0 <= ny && ny < M))) continue;
            if((field[nx][ny] == 1))
            {
                field[nx][ny] = field[cx][cy] + 1;
                q.push(make_pair(nx, ny));
            }
        }
    }
    printf("%d", field[N-1][M-1]);
}