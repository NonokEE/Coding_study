import sys
ip = sys.stdin.readline

V, E = map(int, ip().split())
K = int(ip())

adj_list = {i:{} for i in range(V+1)}
for _ in range(E):
    u, v, w = map(int, ip().split())
    try :
        adj_list[u][v] = min(adj_list[u][v], w)
    except:
        adj_list[u][v] = w

#dijkstra
import heapq
INF = sys.maxsize

cost = [INF] * (V+1)
cost[K] = 0
heap = []
heapq.heappush(heap, (0, K))

while heap:
    val, cur = heapq.heappop(heap)

    if cost[cur] < val:
        continue

    for node in adj_list[cur].keys():
        if cost[node] > val + adj_list[cur][node]:
            cost[node] = val + adj_list[cur][node]
            heapq.heappush(heap, (cost[node], node))
        
for i in range(1, len(cost)):
    if cost[i] == INF:
        print("INF")
    else:
        print(cost[i])


''' 최단경로
시간 1초 메모리 256MB

방향그래프 가지고 시작점에서 모든 정점으로의 최단 경로를 구하라.
가둥치는 10 이하 자연수임.

- 입력 -
첫 줄에 정점개수 V, 간선개수 E (V는 1이상 20000이하, E는 1이상 300,000이하) (정점 번호는 1부터 V까지)
둘째 줄에 시작정점 번호 K
셋째줄부터 E개동안 u v w = u에서 v로가는 w짜리 간선 (u != v) (중복 간선 있을 수 있음)

- 출력-
첫줄부터 V개동안, i번 정점으로의 최단경로를 출력.
시작점의 경우는 0, 경로가 없으면 INF

--1트--: 결과
모든 정점의 모든 경로를 할 필요는 없으니까 플워는 아니고,
그냥 다익스트라한번 돌리는게 맞는거같다.
V가 너무 커서 인접 행렬 쓰긴 어려움
'''