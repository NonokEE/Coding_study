import sys
ip = sys.stdin.readline

V, E = map(int, ip().split())
K = int(ip())

adj_list = {i:{} for i in range(V+1)}
for _ in range(E):
    u, v, w = map(int, ip().split())
    try: adj_list[u][v] = min(w, adj_list[u][v])
    except: adj_list[u][v] = w

# dijkstra
import heapq         #루프에서 최단거리를 사용하기 위해 힙을 import
INF = sys.maxsize

cost = [INF] * (V+1) #cost[i] = 시작점부터 i까지 가는데 걸리는 weight. 전부 INF로 초기화하고 시작
cost[K] = 0          #시작점만 0으로 초기화한다.
heap = []
heapq.heappush(heap, (0, K)) # heap의 내용은 (weight, V), 특정 루트에서 V까지 가는데 weight만큼 걸린다는 의미.

while heap:
    cur_weight, cur_node = heapq.heappop(heap)   #힙으로 pop하기 때문에 weight가 가장 작은것이 pop된다.

    if cur_weight > cost[cur_node]: #지금 꺼낸 값은 과거시점이고, 다른 루프에서 cost값이 갱신되어있을 수 있다. 
        continue                    #갱신된 값이 과거시점의 현재값보다 작다면 현재값은 쓸모없다.

    for another_node in adj_list[cur_node]: #현재 노드들로부터 다른 노드까지 가는데 걸리는 weight를 갱신
        if cost[another_node] > cur_weight + adj_list[cur_node][another_node]: #다른 노드의 현재 값과, 지금의 노드에서 가중치를 더한 값을 비교
            cost[another_node] = cur_weight + adj_list[cur_node][another_node] #cost를 갱신해주고
            heapq.heappush(heap, (cost[another_node], another_node))           #현재루프 시점에서의 최저값과 목적지를 힙에 push

print(cost) 
