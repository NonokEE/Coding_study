import sys
ip = sys.stdin.readline

N = int(ip())

INF = sys.maxsize
adj_mat = [[INF] * N for _ in range(N)]

for _ in range(N-1):
    v1, v2, w = map(int, ip().split())
    v1, v2 = v1-1, v2-1
    adj_mat[v1][v2] = w
    adj_mat[v2][v1] = w

for i in range(N):
    adj_mat[i][i] = 0

for mid in range(N):
    for s in range(N):
        for e in range(N):
            if adj_mat[s][e] > adj_mat[s][mid] + adj_mat[mid][e]:
                adj_mat[s][e] = adj_mat[s][mid] + adj_mat[mid][e]

res = []
for line in adj_mat:
    res.append(max(line))
print(max(res))


#dijkstra

''' 트리의 지름
시간 2초 메모리 128MB

가중치 있는 트리 그래프에서 가장 긴 경로를 출력하셈.

- 입력 -
첫 줄에 노드 개수 n, 1이상 10,000이하
둘째줄부터 부모, 자식, 가중치. 가중치는 100이하의 자연수
루트는 항상 1임

- 출력-
트리의 지름을 출력

--1트--: 결과
트리라서 DFS인 척 하는데, 다익스트라로 해결하면 그만 아닌가 싶음.
루트에서 다익스트라 돌린 다음에 1,2번째로 긴거 출력하면 되는거 아닌가?
ㄴㄴ 그게 쫙 펴지는 경우는 아니라서..
모든 노드에서 다익스트라 돌려서 -> 플로이드 워셜
값 제일 큰거 뽑으면 될듯?
이거 안되면 DFS...인데 노드 개수 너무 많아서 플로이드 워셜 힘들지 않나
'''