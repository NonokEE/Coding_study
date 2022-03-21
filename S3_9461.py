import sys
ip = sys.stdin.readline

DP = [0,1,1,1,2,2,3,4,5,7,9]
DPlen = 10
T = int(ip())
for _ in range(T):
    N = int(ip())
    while DPlen < N:
        DPlen += 1
        DP.append(DP[DPlen-1] + DP[DPlen-5])
    print(DP[N])

''' 파도반 수열
이미지처럼 삼각형 늘어나는데, P(N) 구해라
첫 줄에 TC개수 T, 그 이후에는 N

--1트-- : 정답
그냥 bottom up DP.
DP(N) = DP(N-1) + DP(N-5)
'''