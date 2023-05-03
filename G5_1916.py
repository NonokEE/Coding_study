import sys
ip = sys.stdin.readline

n = int(ip())
m = int(ip())
INF = 99999999

field = [[INF for _ in range(n)] for _ in range(n)]

for _ in range(m):
    s, e, c = map(int, ip().split())
    s-=1
    e-=1
    field[s][e] = c

depart, dest = map(int, ip().split())
depart-=1
dest-=1

for mid in range(n):
    for s in range(n):
        for e in range(n):
            field[s][e] = min(field[s][e], (field[s][mid] + field[mid][e]))

print(field[depart][dest])



''' 최소비용 구하기
시간 0.5초 메모리 128MB

N개의 도시가 있고, 한 도시에서 출발해서 다른 도시에 도착하는 M개의 버스가 있다.
A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화하고 싶다.
도시는 1번부터 N번까지 있음

- 입력 -
첫 줄에 도시 N개 (1개 이상 1,000개 이하)
둘째 줄에 버스 M개 (1개 이상 100,000개 이하)
그 이후부터 버스 노선 정보: 출발도시 도착도시 비용 (비용은 0이상 100,000이하)
마지막 줄에 목적지 출발점과 도착점. (가능한 경우만 주어짐)

--1트--: 시간초과
방향이 있는 그래프고 비용이 있네.
플로이드 워셜이네?
근데 시간이 빡빡한데 되려나 이거?
일단 구현 해보고 생각해봅시다.
사실 플로이드 워셜을 쓰더라도 모든 경로를 구할 필요는 없어서, 출발점에서 끝점까지 가능한 경로만 세어봐도 됨
개조 플로이드 워셜 정도랄까
'''