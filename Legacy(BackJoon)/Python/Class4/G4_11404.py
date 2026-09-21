import sys
ip = sys.stdin.readline

INF = 100000000

N = int(ip())
adj_list = [[INF]*N for _ in range(N)]
for _ in range(int(ip())):
    a, b, c = map(int, ip().split())
    a -= 1
    b -= 1
    adj_list[a][b] = min(adj_list[a][b], c)

for i in range(N):
    adj_list[i][i] = 0

for mid in range(N):
    for s in range(N):
        for e in range(N):
            if adj_list[s][e] > adj_list[s][mid] + adj_list[mid][e]:
                adj_list[s][e] = adj_list[s][mid] + adj_list[mid][e]

for i in range(N):
    for j in range(N):
        if adj_list[i][j] >= INF:
            adj_list[i][j] = 0

for line in adj_list:
    print(*line)

''' 플로이드
시간 1초 메모리 256MB

n개의 도시가 있고, 한 도시에서 출발해서 다른 도시에 도착하는 m개의 버스가 있다
각 버스마다 비용 있다.
모든 경로 출력하셈

- 입력 -
첫 줄에 도시 개수 n (2이상 100이하)
둘째줄에 버스 개수 m (1이상 100,000이하)

이후 노선 정보 a b c = 시작 도착 비용
시작이랑 도착이 같은 경우는 없고, 비용은 100,000이하의 자연수
중복 입력 가능

- 출력-
인접행렬 출력
자기 자신은 0으로 출력하고, 도달 불가능한 경우에도 0으로 출력

--1트--: 성공
모든 경로니까 볼것도 없이 플로이드 워셜이지. 문제 이름도 플로이드잖아. 시간이 좀 걸리긴 한데 메모리가 딸리진 않을듯.

'''