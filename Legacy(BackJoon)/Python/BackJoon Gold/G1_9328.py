## G1 9328 열쇠
import sys
ip = sys.stdin.readline

## 
from collections import deque
import copy
dx = [0,0,-1,1]
dy = [-1,1,0,0]


for _ in range(int(ip())):
    ## 입력 및 초기화
    h, w = map(int, ip().split())
    res = 0
    
    field = []
    doors = {chr(i):[] for i in range(65, 91)}
    for i in range(h): 
        line = " ".join(ip().strip()).split()
        field.append(line)

        for j in range(w):
            if 65 <= ord(line[j]) < 91: doors[line[j]].append((i,j))

    #열쇠
    keys = set()
    key_ip = ip().strip()
    if key_ip != "0":
        for key in " ".join(key_ip).split(): keys.add(key)

    ## 출발점 처리
    boundarys = set()
    for x in range(h):
        boundarys.add((x,0))
        boundarys.add((x,w-1))

    for y in range(1, w-1):
        boundarys.add((0,y))
        boundarys.add((h-1,y))

    #출발점 특수케이스 전처리
    for bx, by in boundarys:
        #열쇠인 경우 -> .으로 바꾸고 획득처리
        if 97 <= ord(field[bx][by]) < 123:
            keys.add(field[bx][by])
            field[bx][by] = "."

        #$인 경우 -> .으로 바꾸고 득점
        if field[bx][by] == "$":
            res += 1
            field[bx][by] = "."

    #첫 열쇠 전처리
    for key in keys:
        for x,y in doors[chr(ord(key)-32)]: field[x][y] = "."

    #출발점 큐 생성
    q = deque()
    for bx, by in boundarys:
        if field[bx][by] == ".": 
            field[bx][by] = "0"
            q.append((bx,by))

    ## BFS 
    while q:
        cx, cy = q.popleft()

        for dir in range(4):
            nx = cx + dx[dir]
            ny = cy + dy[dir]
            if not((0 <= nx < h) and (0 <= ny < w)): continue

            # 일반 구역
            if field[nx][ny] == ".":
                field[nx][ny] = "0"
                q.append((nx,ny))

            # 문서
            elif field[nx][ny] == "$":
                field[nx][ny] = "0"
                q.append((nx,ny))
                res += 1

            # 열쇠
            elif 97 <= ord(field[nx][ny]) < 123:
                if field[nx][ny] not in keys:
                    keys.add(field[nx][ny])
                    for ox, oy in doors[chr(ord(field[nx][ny])-32)]:
                        field[ox][oy] = "."

                        #개방성 테스트
                        temp_field = copy.deepcopy(field)
                        temp_queue = deque([(ox,oy)])

                        while temp_queue:
                            tcx, tcy = temp_queue.popleft()

                            for tdir in range(4):
                                tnx = tcx + dx[tdir]
                                tny = tcy + dy[tdir]
                                if (not((0 <= tnx < h) and (0 <= tny < w))) or (temp_field[tnx][tny] == "0"): 
                                    field[ox][oy] = "0"
                                    q.append((ox, oy))
                                    break
                                elif (temp_field[tnx][tny] == ".") or (temp_field[tnx][tny] == "$") or (97 <= ord(temp_field[tnx][tny]) < 123):
                                    temp_field[tnx][tny] = "1"
                                    temp_queue.append((tnx, tny))
                        
                field[nx][ny] = "0"
                q.append((nx,ny))

            # 그 외의 경우 = 열리지 않은 문(A~Z), 벽(*), 이미 방문한 곳(0)

    print(res)