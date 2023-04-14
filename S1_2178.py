###
def pfield(field):
    for i in range(len(field)):
        print(field[i], end=" ")
        print()


###
import sys
ip = sys.stdin.readline

n, m = map(int, ip().split())

field = []
for i in range(n): field.append(list(map(int, list(ip().strip()))))

visited = [(0,0)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while visited:
    x, y = visited.pop(0)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < m) and (field[nx][ny] == 1):
            visited.append((nx, ny))
            field[nx][ny] = field[x][y] + 1

print(field[n-1][m-1])


''' 미로 탐색
N,M크기의 배열 미로가 있다

1은 이동할 수 있는 칸, 0은 이동할 수 없는 칸.
(1,1)에서출발해서 (N,M)으로 이동할 때(좌상단에서 우하단으로)지나야 하는 최소의 칸 수를 구하세요(최단경로를 구하세요)

상하좌우로만 이동할 수 있다.
시작 위치와 도착위치도 포함된다.

첫 줄에 N, M (2<= N,M <= 100)
그 다음에 미로 나옴

--1트-- : 결과
BFS같은데 이론만 알고 구현하는 방법을 모릅니다.
특히 2차원 맵 상하좌우 이동에 취약함. 공부부터 하고 풀어보져

큐로 구현한다?
그럼 한번 상하좌우 살필 때 마다 탐색해야되나... 비효율적이긴 한데 방법이 없나
노드 클래스를 만들면 되기야는 할텐데...
! 실제로 많은 풀이에서 역류를 한다. 조건을 길이 1일때로 설정하기 때문에 두번 이상 역류하진 않아서 무한루프는 안생긴다.
  가장 간단하게 해결하는 셈. 하지만 최적화까지 생각한다면 더 효율적으로 만들 수는 있을 것.

일단 떠오르는 이미지는, 물 붓듯이 탐색하는거임.
문제에서는 한번만 탐색하면 되기 때문에 지금 주어진 맵을 바로 뜯어고쳐도 상관 없다.

일단은 내 스타일대로 짜보고, 시간 걸리면 visited큐를 deque로 바꿔주자.

대부분 최단경로 알고리즘은 그래프에다가 숫자 덧칠하는 식으로 진행되는듯.
혹시 나중에 여러번 탐색할 필요가 있다면, 원본 그래프를 복사하는 식으로 진행하자.
'''