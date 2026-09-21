import sys
ip = sys.stdin.readline

# 입력
N, E = map(int, ip().split())
adj_list = {i:[] for i in range(N)}

for _ in range(E):
    s, e, c = map(int, ip().split())
    s, e = s-1, e-1
    adj_list[s].append((e, c))
    adj_list[e].append((s, c))

v1, v2 = map(int, ip().split())
v1, v2 = v1-1, v2-1

# 다익스트라 함수
import heapq
INF = sys.maxsize

def diikstra(s):
    cost = [INF] * N
    cost[s] = 0
    heap = []
    heapq.heappush(heap, (0, s))

    while heap:
        val, cur = heapq.heappop(heap)
        if cost[cur] < val: 
            continue

        for e, c in adj_list[cur]:
            if cost[e] > val + c:
                cost[e] = val + c
                heapq.heappush(heap, (cost[e], e))

    return cost

# 경로 찾기
route_0 = diikstra(0)
route_v1 = diikstra(v1)
route_v2 = diikstra(v2)

s_v1_v2_e = route_0[v1] + route_v1[v2] + route_v2[N-1]
s_v2_v1_e = route_0[v2] + route_v2[v1] + route_v1[N-1]
res = min(s_v1_v2_e, s_v2_v1_e)

print(res if (res < INF) else -1)

''' 특정한 최단 경로
시간 1초 메모리 256MB

방향없는 그래프가 주어진다. 
1번 노드에서 N번 노드로 최단거리로 이동할건데, 임의로 주어진 두 정점은 반드시 통과해야된다.
한번 이동했던 정점이나 간선 모두 다시 쓸 수 있다. 

- 입력 -
첫 줄에 정점 개수 N과 간선 개수 E (N은 2이상 800이하, E는 0이상? 200,000이하)
그 이후로 E개동안 a에서 b까지 거리 c (중복 간선은 없음)
마지막으로 무조건 거쳐야하는 v1과 v2.
v1 != v2이고, v1은 마지막 정점이 될 수 없으며 v2는 첫 정점이 될 수 없다. 
(v1가 1이 될 수는 있고, v2가 N이 될 수는 있다.)

- 출력-
최단경로를 출력.
경로가 없으면 -1 출력.

--1트--: 다익스트라 공부
다익스트라와 플로이드 워셜의 차이는 무엇이냐?
플로이드 워셜은 모든 노드에 대해 모든 최단 경로를 구하는거고
다익스트라는 하나의 노드로무터 모든 최단 경로를 구하는거다.

일단 경로를 알아야겠는데. 
-> ㄴㄴ 가장 v1 v2는 어차피 무조건 거쳐야되는 것. 
최단경로에 껴있으면 알아서 계산 되는거고, 무조건 거친다고 생각하고 경로 계산하면 됨.
'''