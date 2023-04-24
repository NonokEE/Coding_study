def pfield(field:list):
    for i in range(len(field)):
        for j in range(len(field[i])):
            print("%4d"%field[i][j], end=" ")
        print()
###
import sys
ip = sys.stdin.readline
m, n = map(int, ip().split())
field = [list(map(int, ip().split())) for _ in range(n)]

##초기화##
day = 0
buffer = []
for i in range(n):
    for j in range(m):
        if field[i][j] == 1:
            buffer.append((i,j))

old_zeros = 99999999
zeros = 0
for line in field: zeros += line.count(0)

dx = [-1,1,0,0] #상하
dy = [0,0,-1,1] #좌우

##루프##

flag = True # 토마토 전부 순회가 가능한 경우 True, 불가능하면 False

while zeros>0:

    temp_buffer = []

    while buffer:

        x, y = buffer.pop()

        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]

            if (0 <= cx < n) and (0 <= cy < m) and field[cx][cy] == 0:
                temp_buffer.append((cx,cy))
                field[cx][cy] = (day+1)

    buffer = temp_buffer

    old_zeros = zeros
    zeros = 0
    for line in field: zeros += line.count(0)

    if zeros == old_zeros:
        flag = False
        break

    day += 1

if flag: print(day)
else   : print(-1)


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