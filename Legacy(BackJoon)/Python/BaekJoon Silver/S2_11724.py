import sys
ip = sys.stdin.readline

n, m = map(int, ip().split())
adj_mat = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    u,v = map(int, ip().split())
    u -= 1
    v -= 1

    adj_mat[u][v] = 1
    adj_mat[v][u] = 1

visited = [False for _ in range(n)]
res = 0

for i in range(n):
    if not visited[i]:
        visited[i] = True
        res += 1

        dfs_stack = [i]
        while dfs_stack:
            start = dfs_stack.pop()
            for route in range(n):
                if adj_mat[start][route] and (not visited[route]):
                    dfs_stack.append(route)
                    visited[route] = True

print(res)


''' 연결 요소의 개수
시간 3초 메모리 512MB

방향 없는 그래프에서 연결 요소의 개수를 구하라

- 입력 -
첫 줄에 정점의 개수 N과 간선의 개수 M
그 다음부터 간선 양 끝점 u와 v

--1트--: 연결요소가 뭔지 이해가 안되서 그냥 코드로 이해함
아니 그래서 연결요소가 뭔데
그냥 DFS나 구현해놓으면 지가 뭔가 하지 않을까 싶긴 해

순회 중에 방문하지 않은 새 노드인데,
연결된게 없는 외딴 노드라면 연결요소 개수 + 1 하고 방문처리
외딴 노드가 아니라면 거기서부터 BFS or DFS

메모리 넉넉해서 인접행렬로 했는데, 메모리 부족하면 인접리스트 쓰자.
결국 이해한거랑 맞긴 한데... 왜 그림으로 그리면 이해가 안되지

'''