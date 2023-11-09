###
def pmap(map):
    for i in range(len(map)):
        for j in range(len(map)):
            if map[i][j] == INF: print("  INF", end=" ")
            else               : print("%5d"%map[i][j], end=" ")
        print()
###
import sys
ip = sys.stdin.readline
INF = 99999999

N, M = map(int, ip().split())

## 인접행렬 초기화 ##
relative_map = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c = map(int, ip().split())
    r-=1
    c-=1
    relative_map[r][c] = 1
    relative_map[c][r] = 1

for i in range(N):
    for j in range(N):
        if ((i!=j) and (relative_map[i][j] == 0)): relative_map[i][j] = INF

## 플로이드 워셜 ##
for temp_node in range(N):
    for i in range(N):
        for j in range(N):
            relative_map[i][j] = min(relative_map[i][j], relative_map[i][temp_node] + relative_map[temp_node][j])

## 결과 산출 ##
res = [0 for _ in range(N)]
for i in range(N):
    res[i] = sum(relative_map[i])

min = INF
ans = INF
for i in range(N):
    if res[i] < min:
        min = res[i]
        ans = i

print(ans+1)

''' 케빈 베이컨의 6단계 법칙
임의의 두 사람이 최소 몇 단계만에 이어질 수 있는가? 라는 게임

케빈 베이컨 = 이 게임 했을 때 단계의 총합이 가장 작은 사람
단계의 총합이라는게, 자신 외의 모든 참가자를 대상으로 단계 산출했을 떄 그 숫자의 합이다.

사람 수와 연결 관계가 주어졌을 때, 수가 가장 작은 사람을 구하는 프로그램을 작성하시오. (복수일 경우에는 가장 빠른 번호)

-입력-
첫줄에 유저수와 관계 수(엣지 수) 
둘째줄부터 관계 정보

! 친구가 한 명도 없는 사람은 없다.
! A와 B가 친구면 B와 A도 친구고, A와 B가 동일인물일 수는 없다.
! A-B가 입력으로 들어왔더라도, B-A가 입력으로 들어올 수 있다.
-> 트랜스포스해서 합친 다음에...? 이거 np없이 행렬 합 되나? 아이고 안되는구나
   아무튼 트랜스포스해서 합치고 0만 아니면 됨.

--1트-- : 정답. 플로이드 워셜에 대해서 복습하고 잘 기억합시다.
감이 안잡힙니다! 플로이드 워셜을 검색해봅니다! 이게 공부지

- 플로이드 워셜 -
모든 노드 간 최단 경로를 구하는 알고리즘.

우선 그래프를 인접행렬로 나타낸다. 
각 값은 거리를 의미하며, 길이 없다면 무한대값. 1 -> 1은 0임

ex)

0     5   inf     9     1
5     0     2   inf   inf
inf   2     0     7   inf
9   inf     7     0     2
1   inf   inf     2     0

각각의 노드를 "중간 노드"로 선택하는 "라운드"를 실행한다. 
즉, 노드가 5개라면 라운드는 총 5회.

round 1:
1 라운드에는 1번 노드를 "중간 노드"로 선택한다.
2-4는 원래 없지만, 1이 중간노드가 되어주면 2-1-4로 5+9의 길이 생긴다. 이 값을 2-4로 갱신해준다.

0     5   inf     9     1
5     0     2    14   inf
inf   2     0     7   inf
9    14     7     0     2
1   inf   inf     2     0

마찬가지로 2-5도 없었는데, 2-1-5가 생겼으므로  5+1의 길이 생긴다.

0     5   inf     9     1
5     0     2    14     6
inf   2     0     7   inf
9    14     7     0     2
1     6   inf     2     0

round 2:
이번엔 2번 노드가 중간 노드가 된다.
1-3이 없는데, 2-3이 있으므로 1-2-3이 생긴다. 
그리고 3-5도 없는데 round 1에서 2-5가 생겼으므로 2-3-5도 생긴다.

0     5     7     9     1
5     0     2    14     6
7     2     0     7     8
9    14     7     0     2
1     6     8     2     0

이런 식으로 모든 노드를 중간 노드로 하면 모든 노드 간 최단 거리를 구할 수 있다.
간단한 예시라서 길 이어주기만 했는데, 우회 경로가 직통 경로보다 가깝거나 하는 경우도 있을 수 있기 때문에 각 길을 비교하는 식으로 구현한다.

--
O^3짜리라서 시간 모자라면 못쓴다고 합니다.

'''