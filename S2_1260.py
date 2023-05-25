import sys
ip = sys.stdin.readline

N, M, V = map(int, ip().split())
graph = {i:[] for i in range(1, N+1)}

for _ in range(M):
    v1, v2 = map(int, ip().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for arr in graph.values():
    arr.sort()

#DFS
visited = [False for _ in range(N+1)]
def DFS(cur):
    if visited[cur]:
        return
    visited[cur] = True
    print(cur, end=" ")
    for e in graph[cur]:
        DFS(e)
DFS(V)
print()

#BFS
from collections import deque
visited = [False for _ in range(N+1)]
queue = deque([V])

while queue:
    cur = queue.popleft()
    if not visited[cur]:
        visited[cur] = True
        print(cur, end=" ")
        queue += deque(graph[cur])


''' DFS와 BFS
시간 2초 메모리 128MB

DFS순회 결과랑 BFS순회 결과를 출력하세요.

- 입력 -
첫 줄에 정점개수 N, 간선개수 M, 시작점 V
다음 M개 동안 연결정보. 연결들은 양방향이고 중복입력도 들어올 수 있음.

정점 개수는 1개이상 1,000개 이하, 간선 개수는 1개 이상 10,000개 이하

- 출력-
V로 시작했을 때,
DFS결과
BFS결과

--1트--: 결과
정점 최대 1000개니까 인접리스트로 하죠
재귀 안쓰는걸로 구현하면 정답의 출력이 안나옴;
'''