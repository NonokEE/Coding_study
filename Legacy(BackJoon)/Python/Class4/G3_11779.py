## G3 11779 최소비용 구하기 2
import sys
ip = sys.stdin.readline

num_v = int(ip())
num_e = int(ip())
G = [[] for _ in range(num_v)]

for _ in range (num_e):
    s, e, t = map(int, ip().split())
    s -= 1
    e -= 1
    G[s].append((e, t))

start_point, end_point = map(int, ip().split())
start_point -= 1
end_point -= 1

## 다익스트라
import heapq

INF = sys.maxsize
dist = [INF] * num_v
prev_node = [0] * num_v

dist[start_point] = 0
queue = []
heapq.heappush(queue, (0, start_point))

while queue:
    cur_cost, cur_node = heapq.heappop(queue)
    if dist[cur_node] < cur_cost: continue

    for next_node, next_cost in G[cur_node]:
        if dist[next_node] >= cur_cost + next_cost:
            dist[next_node] = cur_cost + next_cost
            heapq.heappush(queue, (cur_cost + next_cost, next_node))

            prev_node[next_node] = cur_node

## 경로 계산
path = [end_point]
cur = end_point
while cur != start_point:
    cur = prev_node[cur]
    path.append(cur)

path.reverse()

## 출력
print(dist[end_point])
print(len(path))
print(" ".join(map(lambda x: str(x+1), path)))
