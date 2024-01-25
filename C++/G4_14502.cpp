//G4 14502 연구소
#include <iostream>
using namespace std;
//
#include<vector>
#include<queue>

int n, m;
int original[8][8];
int simulation[8][8];
int temp[8][8];
int res = 0;

vector<pair<int,int>> virus;
vector<pair<int,int>> candidate;
int cand_size;
bool visited[8][8];
vector<pair<int,int>> selected;
//
void arr_copy(int copy_this[][8], int to_here[][8])
{
    for(int i = 0 ; i < n ; i++)
        for(int j = 0 ; j < m ; j++)
            to_here[i][j] = copy_this[i][j];
}
//
bool is_infield(int x, int y) { return (0 <= x) && (x < n) && (0<= y) && (y < m); }

int dx[4] = {-1,1,0,0};
int dy[4] = {0,0,-1,1};

void spread_virus(int field[][8])
{
    queue<pair<int,int>> q;
    for(auto e = virus.begin() ; e != virus.end() ; ++e) q.push(*e);

    while(! q.empty())
    {
        int cx = q.front().first;
        int cy = q.front().second;
        q.pop();

        for(int dir = 0 ; dir < 4 ; dir++)
        {
            int nx = cx + dx[dir];
            int ny = cy + dy[dir];

            if ((is_infield(nx,ny)) && (field[nx][ny] == 0))
            {
                field[nx][ny] = 3;
                q.emplace(nx,ny);
            }
        }
    }
}
//
int count_safe(int field[][8])
{
    int val = 0;
    for(int i = 0 ; i < n ; i++)
        for(int j = 0 ; j < m ; j++)
            if(field[i][j] == 0) val++;
    return val;
}

void back_tracking(int cand_index)
{
    if(selected.size() == 3)
    {
        arr_copy(original, temp);
        for(auto e = selected.begin() ; e != selected.end() ; ++e) temp[e->first][e->second] = 1;
        spread_virus(temp);
        res = max(res, count_safe(temp));
        return;
    }

    for(int i = cand_index ; i < cand_size ; i++)
    {
        int x = candidate[i].first;
        int y = candidate[i].second;

        if(visited[x][y] == true) continue;

        visited[x][y] = true;
        selected.emplace_back(x,y);

        back_tracking(i);

        visited[x][y] = false;
        selected.pop_back();
    }
}
//
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n >> m;
    for(int i = 0 ; i < n ; i++)
        for(int j = 0 ; j < m ; j++)
        {
            cin >> original[i][j];
            if(original[i][j] == 2) virus.emplace_back(i,j);
        }
    //

    arr_copy(original, simulation);
    spread_virus(simulation);

    for(int i = 0 ; i < n ; i++)
        for(int j = 0 ; j < m ; j++)
            if(simulation[i][j] == 3) candidate.emplace_back(i,j);
    cand_size = candidate.size();

    //
    back_tracking(0);
    cout << res;
}
