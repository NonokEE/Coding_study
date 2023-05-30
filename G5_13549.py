import sys
ip = sys.stdin.readline

N, K = map(int, ip().split())
INF = 99999999
field = [INF]*100001

from collections import deque
queue = deque([N])
field[N] = 0

def isinfield(num):
    return 0<= num <= 100000
while field[K] == INF:
    cur = queue.popleft()

    tele = 2*cur
    while isinfield(tele) and (field[tele] > field[cur]):
        field[tele] = field[cur]
        queue.append(tele)
        tele = 2*tele

    if isinfield(cur+1) and (field[cur+1] > field[cur] + 1):
        field[cur+1] = field[cur] + 1
        queue.append(cur+1)

    if isinfield(cur-1) and (field[cur-1] > field[cur] + 1):
        field[cur-1] = field[cur] + 1
        queue.append(cur-1)

print(field[K])  

''' 숨바꼭질3
시간 2초 메모리 512MB

수빈이는 점 N에 있고 동생은 점 K에 있다.
수빈이는 1초만에 좌우 한 칸을 걸어가든가 0초만에 2*현재위치로 텔을 탈 수 있다.

몇 초만에 동생 잡을 수 있을까?

- 입력 -

수빈이 위치 N 동생위치 K

- 출력-
최단 시간

--1트--: 결과
BFS겠지? 근데 텔이 0초임 그래도 일단 BFS가 제일 합당해보임.
INF는 100,000 넘으면 됨. 제일 멍청하게가도 저거 안에는 감.
'''