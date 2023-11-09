def pfield(field:list):
    for i in range(len(field)):
        for j in range(len(field[i])):
            print("%4d"%field[i][j], end=" ")
        print()
###
import sys
from collections import deque

ip = sys.stdin.readline
m, n = map(int, ip().split())
field = [list(map(int, ip().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque([])
for i in range(n):
    for j in range(m):
        if field[i][j] == 1:
            queue.append((i,j))

def BFS():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]

            if (0 <= cx < n) and (0 <= cy < m) and field[cx][cy] == 0:      
                field[cx][cy] = field[x][y] + 1
                queue.append((cx,cy))     

BFS()                   

day = 0
for line in field:
    for e in line:
        if e == 0:
            print(-1)
            exit(0)
    day = max(max(line), day)
print(day-1)

''' 틈메이러
M*N크기 격자 상자에 토마토를 하나씩 넣어서 보관한다.
잘 익은 토마토도 있는데, 아직 안 익은 토마토도 있다. 
안 익은 토마토는 잘 익은 토마토 근처에 있게되면 익는다. 근처는 상하좌우.
토마토는 지 혼자 익지 않는다. 며칠이 지나야 전부 다 익는지 알고싶다.

- 입력 -
첫 줄에 M, N
그 이후로 맵 정보 나타나는데 1은 익은 토마토, 0은 안익은 토마토, -1은 토마토 없음

모두 익기까지 걸리는 날 수를 출력하되, 
처음부터 다 익어있으면 0
어떻게 해도 토마토가 모두 익지 못하는 경우는 -1 출력

시간 1초 메모리 256MB

--3트--:
지금 방식은 엄밀하게는 BFS가 아니다
왜냐? 1로 시작했던 부분들 개별적으로 BFS를 시행하니까 전체적으로는 BFS가 아님
전체적으로 BFS를 하면 개별 BFS를 할 때처럼 겹치는 영역을 검사할 필요도 없어서 필요없는 연산을 줄일 수 있음.
1로 시작하는 부분을 전부 BFS 큐에 넣어주면 그게 BFS 1단계 루프인 셈이다.

!! list의 pop(0)이 O(n)이고, deque의 popleft()가 O(1)이랩니다. 

--2트--: 또 시간 초과
그냥 저번에 아파트 단지처럼 모든 칸에 대해서 BFS하는게 나을 것 같은데?
한번 싹 돌리고 나서 결과에 0이 있으면 -1출력하면 그만이고, 그냥 최댓값 출력하면 됨

대신 퍼지는 영역이 중첩될 수도 있는데, 그 때는 더 작은 값이 이기도록 하면 됨

--1트--: 시간 초과
모두 익지 못하는 경우가 있어서 BFS 한방에 알 수는 없을 것 같고, 단지 문제처럼 가능한 모든 칸에 시행해봐야 할 것 같음.
근데 그러자니 토마토가 끝에 쳐박혀있으면 곤란해진단 말이지

하루하루 경과하는 식으로 구현해도 될 것 같긴 하다.
시간이 문제임

0. day0으로 시작, day+1의 위치를 기억하고 시작
loop: 0의 개수가 0개가 되거나, 0의 개수가 바뀌지 않을 때 까지
1. 기억된 위치의 상하좌우를 새로 기억하고 day+1로 바꿔줌
2. day+1
3. 0개수 세기, 이전 시차의 0 개수도 기억하고 있어야함.

이게 구현은 될 것 같은데, 시간이 빡빡함.
일단 이걸로 안되면 플로이드 워셜로 해보는데, 그게 시간이 더 오래 걸리지 않나?
'''