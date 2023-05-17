import sys
ip = sys.stdin.readline

tc = int(ip())

for _ in range(tc):
    n = int(ip())
    stickers = [list(map(int,ip().split()))for _ in range(2)]

    dp = [0, 0]
    last1 = [0,0]
    last2 = [0,0]

    for i in range(n):
        if i > 0:
            dp[0] = stickers[0][i] + max(stickers[1][i-1] + last2[0], last2[1])
            dp[1] = stickers[1][i] + max(stickers[0][i-1] + last2[1], last2[0])
        else:
            dp[0] = stickers[0][0]
            dp[1] = stickers[1][0]

        last2 = last1[:]
        last1 = dp[:]

    print(max(dp))

''' 스티커 
시간 1초 메모리 256MB

스티커 2n개가 있음. 2행 n열로 배치되어있다.
스티커 하나 떼면 변을 공유하는 스티커는 모두 쓸 수 없게 된다.
점수 합이 최대가 되도록 하셈

- 입력 -
첫 줄에 TC개수 T

각 TC 첫 줄에 n (1이상 100,000 미만)
둘째줄부터 점수배치

- 출력-
TC별로 최대값 출력

--1트--: 틀?
피라미드나 RGB같은거에서 했듯이, 경우의 수를 모두 모양으로 만들어줘야됨

- 지금것 1열 + 이전것 2열 + 그전것 1열
- 지금것 1열 + 그전것 2열

'''