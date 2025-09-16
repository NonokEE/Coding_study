## G4 1197 최소 스패닝 트리
import sys
ip = sys.stdin.readline

## 입력
V, E = map(int, ip().split())

adj_list = {i:[] for i in range(V+1)}
for _ in range(E):
    a, b, c = map(int, ip().split())
    adj_list[a].append([c, b])
    adj_list[b].append([c, a])

## Prim Algorithm
import heapq
available = [[0, 1]]       # 임의의 시작점에서 시작. 1이 항상 있으므로 1에서 시작.
visited = [False] * (V+1)
visit_count = 0

res = 0

while available:
    if visit_count == V: break

    cost, next_v = heapq.heappop(available)
    if not visited[next_v]:
        visited[next_v] = True
        visit_count += 1
        res += cost

        for edge in adj_list[next_v]: heapq.heappush(available, edge)

print(res)