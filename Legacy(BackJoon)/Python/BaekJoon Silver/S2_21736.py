import sys
ip = sys.stdin.readline

HEIGHT, WIDTH = map(int, ip().split())
field = [ip().strip() for _ in range(HEIGHT)]

for x in range(HEIGHT):
    for y in range(WIDTH):
        if field[x][y] == 'I':
            sx, sy = x, y
            break

visited = [[False]*WIDTH for _ in range(HEIGHT)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

from collections import deque
q = deque([(sx, sy)])
count = 0

def isInField(x,y):
    return (0 <= x < HEIGHT) and (0 <= y < WIDTH)

while q:
    x, y = q.popleft()
    if not visited[x][y]:
        visited[x][y] = True

        if field[x][y] == 'P':
            count += 1

        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]

            if isInField(cx, cy) and (not visited[cx][cy]) and field[cx][cy] != 'X':
                q.append((cx,cy))

if count: print(count)
else: print("TT")


''' 헌내기는 친구가 필요해
시간 2초 메모리 1024MB

N, M크기의 캠퍼스에서 상하좌우로 이동할 수 있다.
만날 수 있는 사람의 수를 출력하셈

- 입력 -
첫 줄에 캠퍼스 높이, 폭 (둘 다 1이상 600이하)
둘째줄부터 캠퍼스 정보. O는 맨땅, X는 벽, I는 시작, P는 점수.

- 출력-
만난 사람 수를 출력. 아무도 못만나면 TT 출력

--1트--: 결과
1트 시도 내용 및 메모
'''