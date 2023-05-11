import sys
ip = sys.stdin.readline

n = int(ip())

dp = [0,0,0]
last = [0,0,0]

for _ in range(n):
    r,g,b = map(int, ip().split())

    for i in range(3):
        if i == 0: #r
            dp[0] = r + min(last[1], last[2])
        elif i == 1:
            dp[1] = g + min(last[0], last[2])
        else:
            dp[2] = b + min(last[0], last[1])

    last = dp[:]

print(min(dp))
            
''' RGB거리
시간 0.5초 메모리 128MB

집이 N개 있고, 거리는 선분으로 나타낼 수 있다. 1번부터 N번 집이 순서대로 있다
집을 RGB중 하나로 칠해야됨. 집의 각 색별 비용이 주어졌을 때, 비용 최솟값 구하라
 * 1번집은 2번집이랑 달라야 함
 * N번집은 N-1번집이랑 달라야 함
 * i번집은 i-1번집, i+1번집과 달라야함.
즉, 연속으로 같은 색이면 안된다는 이야기.

- 입력 -
첫 줄에 집 개수 (2이상 1000이하)
둘째줄부터 각 집마다 RGB 칠하는 비용

- 출력 - 
최소비용

--1트--: 
간단한 DP 연속으로 같은 색만 아니면 되니까, 직전 선택만 생각하면 됨. 하나짜리 점화식이라는 얘기

'''