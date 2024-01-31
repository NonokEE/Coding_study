import sys
ip = sys.stdin.readline

V = int(ip())
adj_list = {i:{} for i in range(V+1)}

for _ in range(V):
    v1, *info, _ = list(map(int, ip().split()))

    for i in range(len(info)//2):
        v2 = info[i*2]
        w = info[i*2 + 1]

        adj_list[v1][v2] = w
        adj_list[v2][v1] = w

def DFS(s):
    stack = [(s, 0)]
    visited = [False]*(V+1)

    farthest_node = 0
    farthest_weight = 0

    while stack:
        cur, weight = stack.pop()

        if weight > farthest_weight:
            farthest_node = cur
            farthest_weight = weight

        if not visited[cur]:
            visited[cur] = True
            
            for next_node in adj_list[cur].keys():
                if not visited[next_node]:
                    stack.append((next_node, weight + adj_list[cur][next_node]))

    return (farthest_node, farthest_weight)

v1, w1 = DFS(1)
v2, w2 = DFS(v1)
print(w2)

''' 트리의 지름
시간 2초 메모리 256MB

트리의 지름을 구해라.
문제에서 정점 번호는 1부터 V까지임.

- 입력 -
정점 개수 V(2이상 100,000이하)
각 줄에 연결정보

- 출력-
지름 출력

--1트--: 이게 뭔 G2야
G4문제랑 다르게 루트가 어딘지는 모르고, 자식이 2개보다 많을 수도 있음.
근데 크게 다르려나?
트리니까 둥글게둥글게 안되겠지?
'''