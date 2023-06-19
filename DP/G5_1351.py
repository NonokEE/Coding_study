import sys
ip = sys.stdin.readline

N, P, Q = map(int, ip().split())

stack = [N]
count = 0

while stack:
    cur = stack.pop()
    if cur == 0:
        count += 1
    elif cur == 1:
        count += 2
    else:
        stack.append(int(cur/P))
        stack.append(int(cur/Q))

print(count)
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
재귀로 하면 걸리는 케이스가 있는거 같음.

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