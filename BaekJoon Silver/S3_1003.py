import sys
ip = sys.stdin.readline

T = int(ip())

fzero = [1, 0]
fone = [0, 1]
f_val = 2

for _ in range(T):
    N = int(ip())
    while f_val <= N:
        fzero.append(fzero[f_val-1] + fzero[f_val-2])
        fone.append(fone[f_val-1] + fone[f_val-2])
        f_val += 1

    print(fzero[N], fone[N])

'''
피보나치 함수 구현하고, 0이랑 1 각각 몇번 출력되는지.
첫줄에 TC 개수 T
각 TC는 0<=N<=40

--1트-- : 시간초과
그냥 일단 피보나치 구현해보자.

--2트-- : 시간초과
다른 알고리즘을 구현해야할 것 같은데, 아님 전역변수를 그때그때 초기화하지 말고 인자로 넘겨주든지.
후자로 일단 진행.

--3트-- : 정답!
피보나치를 그냥 쓸 필요가 없다는 뜻. 결과적으로 그 큰 수로부터 각각 0와 1을 몇번 호출하는지의 규칙만 알면 됨.
원래의 피보나치 함수는 top down인데, bottom up으로 하면 효율적으로 횟수만 구할 수 있을듯.

2 = 1 + 0

3 = 2 +     1
  = 1 + 0 + 1

4 = 3 +         2 
  = 2 +     1 + 1 + 0
  = 1 + 0 + 1 + 1 + 0
'''