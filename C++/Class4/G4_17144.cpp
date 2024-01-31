//G4 17144 미세먼지 안녕!
#include <iostream>
using namespace std;

//
#include <set>
#define MAX 50

int r, c, t;
int field[MAX][MAX];
int cleaner_position = 0;    //무조건 0열이고, 입력이 두 번 들어올거니까 공청기의 아랫부분 좌표임. 즉, (cp-1, 0)과 (cp, 0)이 공청기 위치.

//

void input()
{
    cin >> r >> c >> t;
    for(int x = 0 ; x < r ; x++)
    {
        for(int y = 0 ; y < c ; y++)
        {
            cin >> field[x][y];

            if (field[x][y] == -1) 
            {
                cleaner_position = x;
            }
        }
    }
}

//

int dx[4] = {-1,1,0,0};
int dy[4] = {0,0,-1,1};

bool is_infield(int x, int y)    { return (((0 <= x) && (x < r)) && ((0 <= y) && (y < c)));}
bool is_spreadable(int x, int y) { return is_infield(x, y) && (field[x][y] != -1);}

void spread()
{
    int temp_field[MAX][MAX] = {0,};
    set<pair<int,int>> dust_position;
    //
    for(int x = 0 ; x < r ; x++)
    {
        for(int y = 0 ; y < c ; y++)
        {
            temp_field[x][y] = field[x][y];
            if(field[x][y] > 4) dust_position.insert(make_pair(x,y));
        }
    }
    //
    for(auto e = dust_position.begin() ; e != dust_position.end() ; ++e)
    {
        int cx = e->first;
        int cy = e->second;

        for (int dir = 0 ; dir < 4 ; dir++)
        {
            int nx = cx + dx[dir];
            int ny = cy + dy[dir];

            if (is_spreadable(nx,ny))
            {
                temp_field[nx][ny] += field[cx][cy]/5;
                temp_field[cx][cy] -= field[cx][cy]/5;
            }
        }
        
    }
    //
    for(int x = 0 ; x < r ; x++)
    {
        for(int y = 0 ; y < c ; y++)
        {
            field[x][y] = temp_field[x][y];
        }
    }
}

//

void clean()
{
    //상단
    for(int x = cleaner_position-2 ; x > 0                  ; x--) field[x][0] = field[x-1][0];
    for(int y = 0                  ; y < c-1                ; y++) field[0][y] = field[0][y+1];
    for(int x = 0                  ; x < cleaner_position-1 ; x++) field[x][c-1] = field[x+1][c-1];
    for(int y = c-1                ; y > 1                  ; y--) field[cleaner_position-1][y] = field[cleaner_position-1][y-1];
    field[cleaner_position-1][1] = 0;

    //하단
    for(int x = cleaner_position+1 ; x < r-1              ; x++) field[x][0] = field[x+1][0];
    for(int y = 0                  ; y < c-1              ; y++) field[r-1][y] = field[r-1][y+1];
    for(int x = r-1                ; x > cleaner_position ; x--) field[x][c-1] = field[x-1][c-1];
    for(int y = c-1                ; y > 1                ; y--) field[cleaner_position][y] = field[cleaner_position][y-1];
    field[cleaner_position][1] = 0;
}

//
int get_res()
{
    int res = 2;
    for(int x = 0 ; x < r ; x++)
    {
        for(int y = 0 ; y < c ; y++)
        {
            res += field[x][y];
        }
    }
    return res;
}

//

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    //
    input();
    for(int i = 0; i < t; i++)
    {
        spread();
        clean();
    }
    cout << get_res();

    // DEBUG
    // printf("\n\n");
    // for(int x = 0 ; x < r ; x++)
    // {
    //     for(int y = 0 ; y < c ; y++)
    //     {
    //         printf("%2d ", field[x][y]);
    //     }
    //     printf("\n");
    // }

}
