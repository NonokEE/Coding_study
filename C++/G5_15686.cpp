//G5 15686 치킨배달
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int N, M;
int field[50][50];
int res = 99999999;

vector<pair<int, int>> house;
vector<pair<int, int>> chicken;
vector<pair<int, int>> combination;
bool selected[13] = {0};

//
int get_distance(pair<int, int> a, pair<int, int> b)
{
    return abs(a.first - b.first) + abs(a.second - b.second);
}

int get_city_chicken_distance()
{
    int val = 0;

    for(auto h = house.begin() ; h < house.end() ; ++h)
    {
        int dist = 99999999;

        for (auto c = combination.begin() ; c < combination.end() ; ++c)
        {
            int test = get_distance(*h, *c);
            dist = min(dist, get_distance(*h, *c));
        }
        
        val += dist;

    }

    return val;
}

void recursive_combination(int comb_index)
{
    if (combination.size() == M)
    {
        res = min(res, get_city_chicken_distance());
        return;
    }
    else
    {
        for(int i = comb_index ; i < chicken.size() ; i++)
        {
            if (selected[i] == true) continue;

            selected[i] = true;
            combination.push_back(chicken[i]);
            recursive_combination(i);
            selected[i] = false;
            combination.pop_back();
        }
    }
}

//

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    // 입력
    scanf("%d %d", &N, &M);

    for (int x = 0; x < N ; x++)
    {
        for (int y = 0; y < N ; y++)
        {
            scanf("%d", &field[x][y]);

            if     (field[x][y] == 1) house.push_back(make_pair(x,y));
            else if(field[x][y] == 2) chicken.push_back(make_pair(x,y));
        }
    }

    //

    recursive_combination(0);
    printf("%d", res);
}

