import sys
ip = sys.stdin.readline

N, K = map(int, ip().split())
coins = []
for _ in range(N): coins.append(int(ip()))

coins.reverse()
res = 0

for i in range(N):
    if coins[i] > K: continue
    else:
        res += (K//coins[i])
        K = K%coins[i]
    if K == 0: break

print(res)
    

''' 동전 0
N = 동전의 종류, K = 목표 금액
N K 입력 이후
동전 종류 좌라락

--1트-- : 시간초과
그냥 제일 큰거부터 쓰면 되는거 아님? 아님 DP인가?
일단 해보고 아니면 DP임.

--2트--: 성공ㅋㅋ
DP 하기전에, 저거 수식이 좀 무식하지 않나.
%랑 //써도 될 것 같은데 while 돌림?
'''