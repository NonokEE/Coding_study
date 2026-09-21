//G3 2638 치즈
#include <iostream>
using namespace std;
//
#include <vector>
#include <stack>
int N, M;
int field[100][100];
int field_temp[100][100];

vector<pair<int,int>> cheese;
vector<pair<int,int>> cheese_temp;

int res = 0;
//
bool is_outpost(int x, int y) { return (x == 0) || (x == N-1) || (y == 0) || (y == M-1); }

int dx[4] = {-1,1,0,0};
int dy[4] = {0,0,-1,1};

bool is_air(int x, int y)
{
    bool visited[100][100] = {false, };
    stack<pair<int,int>> s;

    visited[x][y] = true;
    s.push({x,y});

    while(!s.empty())
    {
        int cx = s.top().first;
        int cy = s.top().second;
        s.pop();

        if(is_outpost(cx,cy)) return true;

        for(int dir = 0 ; dir < 4 ; dir++)
        {
            int nx = cx + dx[dir];
            int ny = cy + dy[dir];

            if((!visited[nx][ny]) && (field[nx][ny] == 0))
            {
                visited[nx][ny] = true;
                s.push({nx,ny});
            }
        }
    }
    return false;
}

bool will_melt(int x, int y)
{
    int count = 0;
    for(int dir = 0 ; dir < 4 ; dir++)
    {
        int nx = x + dx[dir];
        int ny = y + dy[dir];

        if((field[nx][ny] == 0) && is_air(nx, ny)) count += 1;
    }

    if (count >= 2) return true;
    else            return false;
}
//
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    // 입력
    cin >> N >> M;

    for(int i = 0 ; i < N ; i++)
    {
        for(int j = 0 ; j < M ; j++)
        {
            int temp;
            cin >> temp;
            field[i][j] = temp;
            if (temp) cheese.push_back({i,j});
        }
    }

    // 치즈 순회
    while(!cheese.empty())
    {
        for(int i = 0 ; i < N ; i++)
            for(int j = 0 ; j < M ; j++)
                field_temp[i][j] = 0;

        for(auto e = cheese.begin() ; e != cheese.end() ; ++e)
        {
            int x = e -> first;
            int y = e -> second;

            if(!will_melt(x,y)) 
            {
                cheese_temp.push_back({x,y});
                field_temp[x][y] = 1;
            }
        }

        cheese.assign(cheese_temp.begin(), cheese_temp.end());
        cheese_temp.clear();

        for(int i = 0 ; i < N ; i++)
            for(int j = 0 ; j < M ; j++)
                field[i][j] = field_temp[i][j];
        
        res += 1;

    }

    // 출력
    cout << res << endl;
}
