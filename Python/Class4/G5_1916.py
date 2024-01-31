import sys
ip = sys.stdin.readline

n = int(ip())
m = int(ip())
INF = 1e9

adj_list = [[] for _ in range(n)]

for _ in range(m):
    s, e, c = map(int, ip().split())
    s-=1
    e-=1
    adj_list[s] += [(e, c)]

depart, dest = map(int, ip().split())
depart-=1
dest-=1

# 다익스트라 초기화 
import heapq
cost = [INF for _ in range(n)]
cost[depart] = 0
heap = []
heapq.heappush(heap, (0, depart))

# 다익스트라 시작 #
while heap:
    val, cur = heapq.heappop(heap)

    if cost[cur] < val: continue

    for e, c in adj_list[cur]:
        if cost[e] > val + c:
            cost[e] = val + c
            heapq.heappush(heap, (cost[e], e))

print(cost[dest])


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

--2트--
모든 경로 구하지 말고, 출발지랑 도착지까지만 해보죠
아 이거 플로이드 워셜이 아니고 다익스트라구나..!
둘을 언제 쓸 지 아는 것도 중요할듯

0. 출발점을 0으로, 나머지를 전부 무한으로 설정
1. 출발점(cur)에 연결되어있고 방문하지 않은 노드들을(연결 리스트 안에 있는 노드: t) 확인
2. cur~t + depart~cur < depart~t 라면 갱신
3. cur에 대해 이걸 수행하고, 가장 짧은 정점을 선택
4. 노드 개수 - 1 만큼 반복수행

일반적으로 인접 리스트로 구현하는게 쉬운듯, 인접 행렬로 구현해도 안될건 없다.
그리고 가장 작은 노드 뽑는 부분에서 힙 쓸 수 있음

--1트--: 시간초과
방향이 있는 그래프고 비용이 있네.
플로이드 워셜이네?
근데 시간이 빡빡한데 되려나 이거?
일단 구현 해보고 생각해봅시다.
사실 플로이드 워셜을 쓰더라도 모든 경로를 구할 필요는 없어서, 출발점에서 끝점까지 가능한 경로만 세어봐도 됨
개조 플로이드 워셜 정도랄까
'''