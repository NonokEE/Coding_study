## G5 2445 별 찍기 - 10
import sys
ip = sys.stdin.readline

sys.setrecursionlimit(10**6)
N = int(ip())
res = [["*"] * N for _ in range(N)]

def recursion(sx, sy, width):
    if width == 1: return

    u = width//3

    for x in range(u + sx, 2*u + sx):
        for y in range(u + sy, 2*u + sy):
            res[x][y] = " "

    recursion(sx      , sy, width//3)
    recursion(sx + u  , sy, width//3)
    recursion(sx + 2*u, sy, width//3)

    recursion(sx      , sy + u  , width//3)
    recursion(sx + 2*u, sy + u, width//3)

    recursion(sx      , sy + 2*u, width//3)
    recursion(sx + u  , sy + 2*u, width//3)
    recursion(sx + 2*u, sy + 2*u, width//3)

recursion(0, 0, N)
for line in res: 
    for e in line:
        print(e, end="")
    print()
