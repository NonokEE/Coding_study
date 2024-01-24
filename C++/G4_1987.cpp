//G4 1987 알파벳
#include <iostream>
using namespace std;

int R, C;
int res = 0;

char field[20][20];
bool visited[26];

int dx[4] = {-1,1,0,0};
int dy[4] = {0,0,-1,1};

//

bool isinfield(int x, int y)
{
    return (((0 <= x) && (x < R)) && ((0 <= y) && (y < C)));
}

void back_tracking(int cx, int cy, int step)
{
    res = max(res, step);

    for(int dir = 0 ; dir < 4; dir++)
    {
        int nx = cx + dx[dir];
        int ny = cy + dy[dir];

        if(isinfield(nx,ny) && !visited[field[nx][ny] - 'A'])
        {
            visited[field[nx][ny] - 'A'] = true;
            back_tracking(nx,ny,step+1);
            visited[field[nx][ny] - 'A'] = false;
        }
    }

}

//

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    //입력
    cin >> R >> C;
    for(int i = 0 ; i < R ; i++)
    {
        for(int j = 0 ; j < C ; j++)
        {
            cin >> field[i][j];
        }
    }
    
    //진행 및 출력
    visited[field[0][0]-'A'] = true;
    back_tracking(0,0,1);
    printf("%d",res);
}
