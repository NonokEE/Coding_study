import sys
ip = sys.stdin.readline

N, P, Q, X, Y = map(int, ip().split())
dp = {}

def rec(n):
   if n <= 0:
      return 1
   elif n in dp:
      return dp[n]
   else:
      dp[n] = rec(((n//P) - X)) + rec((n//Q) - Y)
      return dp[n]

print(rec(N))



''' 무한 수열 2
시간 10초 메모리 512MB???

NPQXY 준다.
Ai = 1
Ai = A(i/p의 버림 - X) + A(l/q의 버림 - Y)

- 입력 -
NPQXY

- 출력-
AN

--1트--:
어제거랑 똑같지?

'''