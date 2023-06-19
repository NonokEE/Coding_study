import sys
ip = sys.stdin.readline

N, P, Q = map(int, ip().split())
arr = [1]

for i in range(1, N+1):
    arr.append(arr[int(i/P)] + arr[int(i/Q)])

print(arr[N])

''' 무한 수열
시간 2초 메모리 128MB

A0 = 1
Ai = A(i/p의 버림) + A(l/q의 버림)
N P Q를 줄테니까 AN을 구해라

- 입력 -
첫 줄에 NPQ

- 출력-
AN

--1트--: TO
기초적인 DP문제. 피보나치랑 똑같이 풀면 될 것 같음.
'''