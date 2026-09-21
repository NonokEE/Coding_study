## G4 2239 스도쿠
import sys
ip = sys.stdin.readline

## 입력
board = []
for _ in range(9):
    board.append(list(map(int, " ".join(ip()).split())))

## 함수 정의
row_hash = [set() for _ in range(9)]
col_hash = [set() for _ in range(9)]
box_hash = [[set() for _ in range(3)] for _ in range(3)]

def write(x, y, num):
    row_hash[x].add(num)
    col_hash[y].add(num)
    box_hash[x//3][y//3].add(num)

def delete(x, y, num):
    row_hash[x].remove(num)
    col_hash[y].remove(num)
    box_hash[x//3][y//3].remove(num)

def is_availabe(x, y, num):
    return (num not in row_hash[x]) and (num not in col_hash[y]) and (num not in box_hash[x//3][y//3])


## 초기화
zeros = []
for i in range(9):
    for j in range(9):
        if board[i][j]: write(i, j, board[i][j])
        else          : zeros.append((i,j))

## 백트래킹
sys.setrecursionlimit(15000)

def back_tracking(index: int):
    if index == len(zeros) - 1 : 
        ##마지막거 처리
        x, y = zeros[index]
        for i in range(1, 10):
            if is_availabe(x, y, i): board[x][y] = i

        ## 출력
        for line in board:
            for e in line: print(e, end="")
            print()
        exit()
    
    x, y = zeros[index]
    for i in range(1, 10):
        if not is_availabe(x, y, i): continue

        board[x][y] = i
        write(x,y,i)

        back_tracking(index+1)

        board[x][y] = 0
        delete(x,y,i)

back_tracking(0)