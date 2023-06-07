import sys
import time
ip = sys.stdin.readline

timescale = 1
iteration = 100000

N = int(ip())
adj_list = {i:{} for i in range(N)}

for _ in range(N-1):
    parent, child, weight = map(int, ip().split())
    parent -= 1
    child -= 1
    adj_list[parent][child] = weight
    adj_list[child][parent] = weight
"""
## DFS case
def DFS (s):
    stack = [(s, 0)]
    visited = [False] * N

    res_node = 0
    res_cost = 0
    while stack:
        cur, val = stack.pop()
        
        if val > res_cost:
            res_cost = val
            res_node = cur

        if not visited[cur]:
            visited[cur] = True
            for child in adj_list[cur].keys():
                if not visited[child]:
                    stack.append((child, val + adj_list[cur][child]))

    return (res_cost, res_node)
###
starttime = time.time() * timescale
for _ in range(iteration):
    cost1, next_node = DFS(0)
    cost2, _ = DFS(next_node)
    endtime = time.time() * timescale
print("DFS: " + str(endtime - starttime))
"""

## Dijkstra case

import heapq
INF = sys.maxsize

def Dijkstra(s):
    cost = [INF] * N
    cost[s] = 0
    
    heap = []
    heapq.heappush(heap, (0, s))

    while heap:
        val, cur = heapq.heappop(heap)

        if val > cost[cur]:
            continue

        for child in adj_list[cur].keys():
            if cost[child] > val + adj_list[cur][child]:
                cost[child] = val + adj_list[cur][child]
                heapq.heappush(heap, (cost[child], child))

    maxval = max(cost)
    maxind = cost.index(maxval)

    return (maxval, maxind)

starttime = time.time() * timescale
for _ in range(iteration):
    cost1, next_node = Dijkstra(0)
    cost2, _ = Dijkstra(next_node)
    endtime = time.time() * timescale
print("Dijkstra: " + str(endtime - starttime))