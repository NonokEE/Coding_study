## G3 1865 웜홀
import sys
ip = sys.stdin.readline

## func
INF = int(1e9)

def bellman_ford(V, E):
    #벨만-포드 초기화
    dist = [INF] * V

    #벨만-포드 시작
    for loop_index in range(V): #벨만-포드에서는 V-1회만큼 시행하지만, 음수 사이클 판별을 위해 1회 더 해야 하므로 총 V회 시행.
        for edge in E:
            u, v, c = edge
            if dist[v] > dist[u] + c: #갱신 조건
                dist[v] = dist[u] + c

                #갱신이 일어났는데 현재 회차가 마지막 회차(=음수 사이클 판별하는 회차)라면 음수 사이클이 존재하는 것.
                if loop_index == V-1: 
                    print("YES")
                    return
    
    print("NO")
    return

## main
TC = int(ip())
for _ in range(TC):
    N, M, W = map(int, ip().split())
    edges = []

    for _ in range(M):
        S, E, T = map(int, ip().split())
        edges.append((S-1 ,E-1 ,T))
        edges.append((E-1 ,S-1 ,T))
    
    for _ in range(W):
        S, E, T = map(int, ip().split())
        edges.append((S-1 ,E-1 ,-T))

    bellman_ford(N, edges)