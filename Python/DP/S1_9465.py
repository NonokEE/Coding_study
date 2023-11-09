import sys
ip = sys.stdin.readline

for _ in range(int(ip())):
    n = int(ip())
    stickers = [list(map(int,ip().split()))for _ in range(2)]

    dp = [0, 0]
    last1 = [0,0]
    last2 = [0,0]

    for i in range(n):
        if i > 0:
            dp[0] = stickers[0][i] + max(last1[1], last2[1])
            dp[1] = stickers[1][i] + max(last1[0], last2[0])
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

--2트--:
쭉 지그재그로 가느냐 하나 건너 뛴 지그재그냐의 차이
1트도 방법이 맞긴 한데, 복잡하게 생각하다가 뭘 실수한듯. 예외가 생기는 경우가 있나봐

인터넷에서 본 것들은 저렇게 필드가 주어져버리면 아예 필드를 갱신시키는 쪽으로 함
메모리 아낄 수 있고 assign시간도 아낄 수 있어서 좋은 듯.
다른 문제들은 한줄 한줄 입력이 들어오니까 실시간 갱신이 효율적인데, 
이 문제는 가로로 입력이 들어와서 필드 초기화부터 해줘야 되니까 그런듯

--1트--: 틀?
피라미드나 RGB같은거에서 했듯이, 경우의 수를 모두 모양으로 만들어줘야됨

- 지금것 1열 + 이전것 2열 + 그전것 1열
- 지금것 1열 + 그전것 2열
'''