## G1 2098 외판원 순회
import sys
ip = sys.stdin.readline

## 입력
N = int(ip())
W = [list(map(int,ip().split())) for _ in range(N)]

## DFS
INF = int(1e9)
DP = {} #분할 정복이나 계산 누적을 통한 문제 해결이 아닌, 연산 절약을 위한 DP라서 단순히 (현재위치, visited배열)을 key로 하는 dictionary로 사용한다.

def DFS(cur, visited):
    #모든 도시를 방문한 경우
    if visited == ((1 << N) - 1):
        if W[cur][0]: return W[cur][0] #출발점으로 돌아갈 수 있는 경우
        else        : return INF       #불가능한 경우 INF 반환하여 채택되지 않게 함.

    #DP체크 (dictionary라서 탐색에는 O(1) 소요)
    if (cur, visited) in DP: return DP[(cur, visited)]

    #DP에 값이 없는 경우 => 계산 진행
    minimum = INF 
    for next in range(1,N):
        #현재 도시에서 다음 도시로 가는 경로가 없거나, 다음 도시를 이미 방문한 경우 continue
        if (W[cur][next] == 0) or (visited & (1<<next)): continue   

        #비용 계산(DFS로 다음 경로 받아와서 값 산출)
        cost = DFS(next, (visited | (1<<next))) + W[cur][next]
        minimum = min(cost, minimum)    #최저값 갱신

    DP[(cur, visited)] = minimum    #DP에 최저값 반영
    return minimum

print(DFS(0, 1))