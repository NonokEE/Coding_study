//G4 14938 서강그라운드
#include <iostream>
using namespace std;
//
#define INF 99999999
int num_v, sight, num_e;
int v_weight[100];
int graph[100][100];

int res = 0;
//
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    //입력 및 초기화
    cin >> num_v >> sight >> num_e;

    for(int v = 0 ; v < num_v ; v++)
        cin >> v_weight[v];


    for(int i = 0 ; i < num_v ; i++)
    {
        for(int j = 0 ; j < num_v ; j++)
            graph[i][j] = INF;
        graph[i][i] = 0;
    }

    for(int e = 0 ; e < num_e ; e++)
    {
        int node1, node2, node_weight;
        cin >> node1 >> node2 >> node_weight;
        graph[node1-1][node2-1] = node_weight;
        graph[node2-1][node1-1] = node_weight;
    }

    //플로이드-워셜
    for(int mid = 0 ; mid < num_v ; mid++)
    {
        for(int s = 0 ; s < num_v ; s++)
        {
            for(int e = 0 ; e < num_v ; e++)
            {
                if(graph[s][e] > graph[s][mid] + graph[mid][e])
                {
                    graph[s][e] = graph[s][mid] + graph[mid][e];
                }
            }
        }
    }

    //
    for(int i = 0 ; i < num_v ; i++)
    {
        int line_res = 0;
        for(int j = 0 ; j < num_v ; j++)
        {
            if(graph[i][j] <= sight) line_res += v_weight[j];
        }
        res = max(line_res, res);
    }
    cout << res << endl;
}
