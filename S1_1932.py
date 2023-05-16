import sys
ip = sys.stdin.readline

n = int(ip())

last = [0]

for lv in range(1, n+1):
    line = list(map(int, ip().split()))

    dp = [0 for _ in range(lv)]
    for i in range(lv):
        dp[i] += line[i]
        if i == 0:
            dp[i] += last[0]
        elif i == lv-1:
            dp[i] += last[i-1]
        else:
            dp[i] += max(last[i-1], last[i])

    last = dp

print(max(dp))

''' 정수 삼각형
시간 2초 메모리 128MB

크기가 n인 정수 삼각형이 있다.
쪼로록 타고 내려가면서 선택한 수의 합이 최대가 되도록 하라.
대각 아래 있는 것만 선택할 수 있음.

- 입력 -
정수 크기 n
삼각형 내용

- 출력-
최대값

--1트--: 결과
       0
     0   1
   0   1   2
 0   1   2   3

0 -> 이전에 0에서만 올 수 있음
1~2 -> 자기 번호 - 1 or 자기 번호에서 올 수 있음
3 -> 자기 번호 - 1에서만 올 수 있음

'''