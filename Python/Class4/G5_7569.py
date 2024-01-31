import sys
from collections import deque

ip = sys.stdin.readline
m, n, h = map(int, ip().split())
field = [[list(map(int, ip().split())) for _ in range(n)] for _ in range(h)]

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

queue = deque([])
for i in range(h):
    for j in range(n):
        for k in range(m):
            if field[i][j][k] == 1:
                queue.append((i,j,k))

def isInField(x,y,z):
    if (0 <= x < h) and (0 <= y < n) and (0 <= z < m):
        return True
    else:
        return False

def BFS():
    while queue:
        x, y, z = queue.popleft()

        for i in range(6):
            cx = x + dx[i]
            cy = y + dy[i]
            cz = z + dz[i]

            if isInField(cx,cy,cz) and field[cx][cy][cz] == 0:      
                field[cx][cy][cz] = field[x][y][z] + 1
                queue.append((cx,cy,cz))     

BFS()                   

day = 0
max_in_line = 0
for plain in field:
    for line in plain:
        for e in line:
            if e == 0:
                print(-1)
                exit(0)
        day = max(max(line), day)

print(day-1)

''' 도마도
시간 1초 메모리 256MB

7576이랑 똑같은데 3D임

- 입력 -
첫 줄에 M N H 가로 세로 높이
M, N은 2 이상 100이하, H는 1이상 100 이하

둘째줄부터는 가장 밑 상자부터 위 상자까지 저장된 토마토 정보

--1트--: ㅋㅋ
날먹 개꿀 ㅋㅋ
'''