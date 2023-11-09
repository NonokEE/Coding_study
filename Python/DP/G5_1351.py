import sys
ip = sys.stdin.readline

N, P, Q = map(int, ip().split())
dp = {0:1}

def rec(n):
    if n in dp:
        return dp[n]
    else:
        dp[n] = rec(n//P) + rec(n//Q)
        return dp[n]

print(rec(N))



''' 무한 수열
시간 2초 메모리 128MB

A0 = 1
Ai = A(i/p의 버림) + A(l/q의 버림)
N P Q를 줄테니까 AN을 구해라

- 입력 -
첫 줄에 NPQ

- 출력-
AN

--3트--:
재귀가 맞긴 한데, 이미 있는 값을 다시 계산해서 쓰는게 손해니까 그 부분에 DP를 쓰는거잖아?
어떤 연속적인 계산에 DP를 응용하는 예인듯.

--2트--:
안되넹 너무 무식한가
이걸 배열 append를 할 필요가? 미리 선언해두면 되지 않나? -> N이 너무 커서 안됨.
PQ의 최소가 2임. 배열에서 절반은 버려진다는거.
P랑 Q가 바뀌기 전까지는 그냥 쭉 넣어도 됨.
아님 재귀로?

재귀도 안되네 뭐임

--1트--: TO
기초적인 DP문제. 피보나치랑 똑같이 풀면 될 것 같음.
'''