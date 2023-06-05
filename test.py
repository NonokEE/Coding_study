import sys
ip = sys.stdin.readline

V, E = map(int, ip().split())
K = int()

adj_list = {i:{} for i in range(V+1)}
for _ in range(E):
    u, v, w = map(int, ip().split())
    try: adj_list[u][v] = min(w, adj_list[u][v])
    except: adj_list[u][v] = w

# dijkstra